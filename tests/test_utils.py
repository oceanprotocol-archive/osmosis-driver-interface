import os
import sys

from osmosis_driver_interface.utils import retrieve_module_path


def test_retrieve_module_path():
    _type = 'data'
    module = 'azure'
    config = './tests/osmosis.ini'
    assert retrieve_module_path(_type=_type, module=module,
                                config=config) == "%s/lib/python3.%s/site-packages/osmosis_%s_driver/%s_plugin.py" % (
               os.getenv('VIRTUAL_ENV'), sys.version_info[1], module, _type)
