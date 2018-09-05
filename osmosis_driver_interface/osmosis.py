from osmosis_driver_interface.utils import start_plugin
from osmosis_driver_interface.constants import COMPUTING, DATA


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
    def __init__(self, file_path=None):
        self.computing_plugin = start_plugin(COMPUTING, file_path)
        self.data_plugin = start_plugin(DATA, file_path)
