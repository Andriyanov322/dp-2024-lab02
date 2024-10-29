from abc import ABC, abstractmethod
from .log_strategy_interface import LogOutput

class LogManager(ABC):
    """Интерфейс для управления процессом логирования, определяющий основные методы логирования."""

    @abstractmethod
    def set_logging_strategy(self, strategy: LogOutput) -> None:
        """Устанавливает стратегию логирования."""
        pass

    @abstractmethod
    def log_event(self, message: str, level: str) -> None:
        """Логирует событие с заданным уровнем."""
        pass

    @abstractmethod
    def log_trace_event(self, message: str) -> None:
        """Логирует событие уровня TRACE."""
        pass

    @abstractmethod
    def log_info_event(self, message: str) -> None:
        """Логирует событие уровня INFO."""
        pass

    @abstractmethod
    def log_warning_event(self, message: str) -> None:
        """Логирует событие уровня WARNING."""
        pass

    @abstractmethod
    def log_error_event(self, message: str) -> None:
        """Логирует событие уровня ERROR."""
        pass

    @abstractmethod
    def log_fatal_event(self, message: str) -> None:
        """Логирует событие уровня FATAL."""
        pass
