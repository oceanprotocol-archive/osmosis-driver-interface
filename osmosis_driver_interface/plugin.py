from abc import ABC, abstractmethod


class AbstractPlugin(ABC):
    """

    """

    @abstractmethod
    def type(self):
        """A string denoting the type of plugin (e.g. Azure)."""

    def upload(self, file):
        ""

    def download(self, file):
        ""

    def list(self):
        ""

    def generate_url(self):
        ""

    def delete(self):
        ""