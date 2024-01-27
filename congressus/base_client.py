from abc import ABC, abstractmethod


class BaseClient(ABC):
    """
    Basically just an interface. Used as a dependency for Queriers because
    programming against the concrete Client causes circular imports.
    """

    @abstractmethod
    def get_domain(self) -> str:
        pass

    @abstractmethod
    def get_key(self) -> str:
        pass
