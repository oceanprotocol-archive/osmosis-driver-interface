#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

import logging

from osmosis_driver_interface.constants import COMPUTING, DATA
from osmosis_driver_interface.log import setup_logging
from osmosis_driver_interface.utils import start_plugin, get_plugin_url_map

setup_logging()
logger = logging.getLogger('Osmosis')


class Osmosis:
    """High-level, plugin-bound Osmosis functions.
    Instantiated with a subclass implementing the ledger plugin
    interface (:class:`~.AbstractPlugin`) that will automatically be
    bound to all top-level functions:
        - :attr:`type` (as a read-only property)
        - :func:`upload`
        - :func:`download`
        - :func:`list`
        - :func:`generate_url`
        - :func:`delete`
    Attributes:
        plugin (Plugin): Bound persistence layer plugin.
    """

    def __init__(self, url, config_file_path=None, ):
        self.computing_plugin = start_plugin(COMPUTING, self.parse_url(url), config_file_path)
        self.data_plugin = start_plugin(DATA, self.parse_url(url), config_file_path)

    @staticmethod
    def parse_url(url):
        """
        Parse the url to decide which driver should be loaded.

        :param url: str
        :return: Module name, str
        """
        _plugin_name = 'on_premise'
        _key = ''
        plugin_map = get_plugin_url_map()
        for key, name in plugin_map.items():
            if key in url:
                _key = key
                _plugin_name = name
                logger.info(f'Loading `{_plugin_name}` driver, url={url}, plugin-key={key}.')
                break

        if not _key:
            logger.info(f'Loading `{_plugin_name}` driver, url={url}.')

        return _plugin_name
