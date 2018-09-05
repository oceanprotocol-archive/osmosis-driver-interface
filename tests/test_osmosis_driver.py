from pytest import raises
from osmosis_driver_interface.utils import parse_config


def test_osmosis_expects_plugin():
    from osmosis_driver_interface.data_plugin import AbstractPlugin
    with raises(TypeError):
        AbstractPlugin()


def test_osmosis_expcects_subclassed_plugin():
    from osmosis_driver_interface.data_plugin import AbstractPlugin

    class NonSubclassPlugin():
        pass

    plugin = NonSubclassPlugin()
    with raises(TypeError):
        AbstractPlugin(plugin)

def test_parse_config():
    config = parse_config('./tests/osmosis.ini')
    assert config['module'] == 'azure'