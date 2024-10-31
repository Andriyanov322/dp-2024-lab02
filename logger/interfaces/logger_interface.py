from abc import ABC, abstractmethod
from .writer_interface import IWriter
from ..log_levels import LogLevel

class LoggerInterface(ABC):
    """Интерфейс для управления процессом логирования, определяющий основной метод логирования."""

    @abstractmethod
    def set_writer(self, writer: IWriter) -> None:
        """
        Устанавливает стратегию записи логов.

        Args:
            writer (IWriter): Новая стратегия вывода для записи логов.
        """
        pass

    @abstractmethod
    def log(self, message: str, level: LogLevel) -> None:
        """
        Логирует сообщение с указанным уровнем.

        Args:
            message (str): Сообщение для записи в лог.
            level (LogLevel): Уровень логирования (по умолчанию INFO).
        """
        pass
