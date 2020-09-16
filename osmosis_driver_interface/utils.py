#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

import configparser
import importlib.machinery
import importlib.util
import logging
import os
import site
import sys

from osmosis_driver_interface.constants import CONFIG_OPTION
from osmosis_driver_interface.exceptions import ConfigError


def parse_config(file_path):
    """Loads the configuration file given as parameter"""
    config_parser = configparser.ConfigParser()
    config_parser.read(file_path)
    plugin_config = {}
    options = config_parser.options(CONFIG_OPTION)
    for option in options:
        try:
            plugin_config[option] = config_parser.get(CONFIG_OPTION, option)
            if plugin_config[option] == -1:
                logging.info(f'skip: {option}')
        except Exception as e:
            logging.error(f'exception on {option}')
            logging.error(str(e))
            plugin_config[option] = None

    return plugin_config


def start_plugin(_type, module, file_path=None):
    """This function initialize the Osmosis plugin"""
    if os.getenv('CONFIG_PATH'):
        file_path = os.getenv('CONFIG_PATH')
    else:
        file_path = file_path

    if file_path is not None:
        config = parse_config(file_path)
        plugin_instance = load_plugin(_type, module, config)
    else:
        plugin_instance = load_plugin(_type, module)

    return plugin_instance


def load_plugin(_type, module='on_premise', config=None):
    module_path = retrieve_module_path(_type, module, config)
    if sys.version_info < (3, 5):
        from importlib.machinery import SourceFileLoader

        mod = SourceFileLoader(f'{_type}_plugin.py', module_path).load_module()
        return mod.Plugin(config)
    else:
        spec = importlib.util.spec_from_file_location(f'{_type}_plugin.py', module_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.Plugin(config)


def retrieve_module_path(_type, module, config=None):
    try:
        if config is not None and 'module.path' in config:
            module_path = f'{config["module.path"]}/{_type}_plugin.py'

        elif os.getenv('VIRTUAL_ENV') is not None:
            module_path = f'{os.getenv("VIRTUAL_ENV")}/lib/python3.{sys.version_info[1]}'\
                f'/site-packages/osmosis_{module}_driver/{_type}_plugin.py'

        else:
            module_path = f'{site.getsitepackages()[0]}/osmosis_{module}_driver/{_type}_plugin.py'

        return module_path
    except Exception:
        raise ConfigError('You should provide a valid config.')
