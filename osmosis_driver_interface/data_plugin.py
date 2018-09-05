from abc import ABC, abstractmethod


class AbstractPlugin(ABC):
    """Abstract interface for all persistence layer plugins.
    Expects the following to be defined by the subclass:
        - :attr:`type` (as a read-only property)
        - :func:`upload`
        - :func:`download`
        - :func:`list`
        - :func:`generate_url`
        - :func:`delete`
        - :func:`copy`
        - :func:`create_directory`
        - :func:`retrieve_availability_proof`
    """

    @abstractmethod
    def type(self):
        """A string denoting the type of plugin (e.g. Azure)."""

    @abstractmethod
    def upload(self, local_file, remote_file):
        """Upload file to a remote resource manager
         Args:
             local_file(str): The path of the file to upload.
             remote_file(str): The path of the resource manager where the file is going to be allocated.
         Raises:
             :exc:`~..OsmosisError`: if the file is not uploaded correctly.

        """

    @abstractmethod
    def download(self, remote_file, local_file):
        """Download file from a remote resource manager
        Args:
             remote_file(str): The path in the resource manager of the file to download from.
             local_file(str): The path to the file to download to..
        Raises:
             :exc:`~..OsmosisError`: if the file is not downloaded correctly.
        """

    @abstractmethod
    def list(self, remote_folder):
        """List all the files of a cloud directory.
        Args:
             remote_folder(str): Name of the directory to list.
        Returns:
            dict: List with the name of the file of a directory.
        Raises:
             :exc:`~..OsmosisError`: if the directory does not exist.
        """

    @abstractmethod
    def generate_url(self, remote_file):
        """Generate a signed url that give access for a period of time to the resource
        Args:
            remote_file(str): The path in the resource manager of the file to give access.
        Raises:
             :exc:`~..OsmosisError`: if the file does not exist or if the action could not be done.
        """

    @abstractmethod
    def delete(self, remote_file):
        """Delete a file of a remote resource manager
        Args:
             remote_file(str): The path in the resource manager of the file to delete..
        Raises:
             :exc:`~..OsmosisError`: if the path does not exist or if the action could not be done.
        """

    @abstractmethod
    def copy(self, source_path, dest_path):
        """Copy file from a path to another path.
         Args:
             source_path(str): The path of the file to be copied.
             dest_path(str): The destination path where the file is going to be allocated.
         Raises:
             :exc:`~..OsmosisError`: if the file is not uploaded correctly.
        """

    @abstractmethod
    def create_directory(self, remote_folder):
        """Create a directory in the resource manager
        Args:
            remote_folder(str): The path of the remote directory
        Raises:
             :exc:`~..OsmosisError`: if the directory already exists.
        """

    @abstractmethod
    def retrieve_availability_proof(self):
        """TBD"""
