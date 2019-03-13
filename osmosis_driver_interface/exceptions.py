"""Custom exceptions for Osmosis"""


#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

class OsmosisError(Exception):
    """Base class for all Osmosis errors."""


class ConfigError(Exception):
    """Base class for all config errors."""


def __init__(self, message='', error=None):
    self.message = message
    self.error = error


def __str__(self):
    return self.message
