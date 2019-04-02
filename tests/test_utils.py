#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

import os
import sys

from osmosis_driver_interface.utils import retrieve_module_path


def test_retrieve_module_path():
    _type = 'data'
    module = 'azure'
    config = './tests/osmosis.ini'
    assert retrieve_module_path(_type=_type, module=module,
                                config=config) == f'{os.getenv("VIRTUAL_ENV")}/lib/python3.{sys.version_info[1]}' \
                                                  f'/site-packages/osmosis_{module}_driver/{_type}_plugin.py'
