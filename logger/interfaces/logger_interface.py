from abc import ABC, abstractmethod
from .writer_interface import Writer

class LoggerInterface(ABC):
    """Интерфейс для управления процессом логирования, определяющий основные методы логирования."""

    @abstractmethod
    def set_writer(self, writer: Writer) -> None:
        """Устанавливает стратегию записи логов."""
        pass

    @abstractmethod
    def log(self, message: str, level: str) -> None:
        """Логирует сообщение с заданным уровнем."""
        pass

    @abstractmethod
    def log_trace(self, message: str) -> None:
        """Логирует сообщение уровня TRACE."""
        pass

    @abstractmethod
    def log_info(self, message: str) -> None:
        """Логирует сообщение уровня INFO."""
        pass

    @abstractmethod
    def log_warning(self, message: str) -> None:
        """Логирует сообщение уровня WARNING."""
        pass

    @abstractmethod
    def log_error(self, message: str) -> None:
        """Логирует сообщение уровня ERROR."""
        pass

    @abstractmethod
    def log_fatal(self, message: str) -> None:
        """Логирует сообщение уровня FATAL."""
        pass
