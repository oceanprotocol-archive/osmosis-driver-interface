from abc import ABC, abstractmethod


class AbstractPlugin(ABC):
    """Abstract interface for all persistence layer plugins.
    Expects the following to be defined by the subclass:
        - :attr:`type` (as a read-only property)
        - :func:`create_vm`
        - :func:`start_vm`
        - :func:`stop_vm`
        - :func:`run_command`
        - :func:`delete_vm`
        - :func:`retrieve_computation_proof`
        - :func:`retrieve_vm_logs`
    """

    @abstractmethod
    def type(self):
        """A string denoting the type of plugin (e.g. Azure)."""

    @abstractmethod
    def create_vm(self, ):
        """Create a container/instance to compute an algorithm inside.
         Args:
         Raises:
             :exc:`~..OsmosisError`: the vm could not be created with this arguments.

        """

    @abstractmethod
    def start_vm(self, instance_name):
        """Start the container/instance.
        Args:
            instance_name(str): The container/instance name
        Raises:
             :exc:`~..OsmosisError`: if the container/instance does not exist.
        """

    @abstractmethod
    def stop_vm(self, instance_name):
        """Stop the container/instance running.
        Args:
             instance_name(str): The container/instance name
        Raises:
             :exc:`~..OsmosisError`: if the container/instance could not be stopped.
        """

    @abstractmethod
    def run_command(self, instance_name, command):
        """Run a command inside of a container/instance.
        Args:
             instance_name(str): The container/instance name
             command(str): The command that you want to run inside the container/instance
        Raises:
             :exc:`~..OsmosisError`: if the container/instance does not exist or if you do not have permissions to run
             this command
        """

    @abstractmethod
    def delete_vm(self, instance_name):
        """Delete a container/instance.
        Args:
             instance_name(str): The container/instance name
        Raises:
             :exc:`~..OsmosisError`: if the container/instance does not exist.
        """

    @abstractmethod
    def retrieve_computation_proof(self, ):
        """TBD"""

    @abstractmethod
    def retrieve_vm_logs(self, ):
        """TBD"""
