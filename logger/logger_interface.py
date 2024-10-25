# logger/logger_interface.py

from abc import ABC, abstractmethod
from .log_strategies import LogStrategy

class LoggerInterface(ABC):
    """Абстрактный интерфейс для логгера, определяющий основные методы логирования."""

    @abstractmethod
    def set_strategy(self, strategy: LogStrategy) -> None:
        """Устанавливает стратегию логирования."""
        pass

    @abstractmethod
    def log(self, message: str, level: str) -> None:
        """Логирует сообщение определённого уровня."""
        pass

    @abstractmethod
    def trace(self, message: str) -> None:
        """Логирует сообщение уровня TRACE."""
        pass

    @abstractmethod
    def info(self, message: str) -> None:
        """Логирует сообщение уровня INFO."""
        pass

    @abstractmethod
    def warn(self, message: str) -> None:
        """Логирует сообщение уровня WARN."""
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        """Логирует сообщение уровня ERROR."""
        pass

    @abstractmethod
    def fatal(self, message: str) -> None:
        """Логирует сообщение уровня FATAL."""
        pass
