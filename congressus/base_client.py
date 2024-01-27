from abc import ABC, abstractmethod


class BaseClient(ABC):
    @abstractmethod
    def get_domain(self) -> str:
        pass

    @abstractmethod
    def get_key(self) -> str:
        pass
