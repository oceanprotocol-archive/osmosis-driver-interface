"""Custom exceptions for Osmosis"""


class OsmosisError(Exception):
    """Base class for all Osmosis errors."""


class ConfigError(Exception):
    """Base class for all config errors."""


def __init__(self, message='', error=None):
    self.message = message
    self.error = error


def __str__(self):
    return self.message
