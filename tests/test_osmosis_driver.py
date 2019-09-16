#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

from pytest import raises

from osmosis_driver_interface.osmosis import Osmosis
from osmosis_driver_interface.utils import parse_config


def test_osmosis_expects_plugin():
    from osmosis_driver_interface.data_plugin import AbstractPlugin
    with raises(TypeError):
        AbstractPlugin()


def test_osmosis_expcects_subclassed_plugin():
    from osmosis_driver_interface.data_plugin import AbstractPlugin

    class NonSubclassPlugin:
        pass

    plugin = NonSubclassPlugin()
    with raises(TypeError):
        AbstractPlugin(plugin)


def test_parse_config():
    config = parse_config('./tests/osmosis.ini')
    assert config['azure.location'] == 'westus'


def test_osmosis_instances():
    osm = Osmosis('http://www.example.com')
    assert osm.data_plugin.type() == 'On premise'
