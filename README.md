[![banner](https://raw.githubusercontent.com/oceanprotocol/art/master/github/repo-banner%402x.png)](https://oceanprotocol.com)

# osmosis-driver-interface

> 💧 A membrane between the decentralized world and centralized world
> [oceanprotocol.com](https://oceanprotocol.com)

[![Build Status](https://travis-ci.com/oceanprotocol/osmosis-driver-interface.svg)](https://travis-ci.com/oceanprotocol/osmosis-driver-interface)
[![PyPI](https://img.shields.io/pypi/v/osmosis-driver-interface.svg)](https://pypi.org/project/osmosis-driver-interface/)
[![GitHub contributors](https://img.shields.io/github/contributors/oceanprotocol/osmosis-driver-interface.svg)](https://github.com/oceanprotocol/osmosis-driver-interface/graphs/contributors)

---
## Table of Contents
  - [How this works](#brief)
  - [Code style](#code-style)
  - [Testing](#testing)
  - [New Version](#new-version)
  - [License](#license)

---

## How this works
This driver interface allows a data service provider such as [provider-py](https://github.com/oceanprotocol/provider-py) 
to work with any cloud backend such as Azure, AWS by using a driver that implements the `osmosis` interface. 

The `osmosis` interface is defined in `data_plugin.py` and `computing_plugin.py`. 
After writing a new driver, add a mapping in `driver_map.json` to allow `osmosis` to identify urls that the 
new driver is suitable to work with. 
The `driver_map` must be defined in the environment variable `OSMOSIS_DRIVER_MAP` using one of these methods:
* export OSMOSIS_DRIVER_MAP="/path/to/driver_map.json"
* export OSMOSIS_DRIVER_MAP='{"core.windows.net": "azure", "ipfs://": "ipfs", "NewProtocol://": "driver-module-name"}'

Load a driver:
* Create Osmosis instance by giving a `url` and `config_file_path` (optional). Note that 
config file is loaded from env var `CONFIG_PATH` if defined and takes precedence over `config_file_path`
* If a config file is used and has a value for the `module.path` option, then 
this path is used to load the osmosis driver regardless of the `url`
* If no `module.path` is defined, the driver module is automatically determined from 
the `url` using the `driver_map` as described above
  * The driver module name should follow the convention of `osmosis_<module-name>_driver`

  
## Code style

The information about code style in python is documented in these two links [python-developer-guide](https://github.com/oceanprotocol/dev-ocean/blob/master/doc/development/python-developer-guide.md)
and [python-style-guide](https://github.com/oceanprotocol/dev-ocean/blob/master/doc/development/python-style-guide.md).
    
## Testing

Automatic tests are setup via Travis, executing `tox`.
Our tests use the pytest framework.

## New Version

The `bumpversion.sh` script helps to bump the project version. You can execute the script using {major|minor|patch} as first argument to bump the version accordingly.

## License

```
Copyright 2018 Ocean Protocol Foundation Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.