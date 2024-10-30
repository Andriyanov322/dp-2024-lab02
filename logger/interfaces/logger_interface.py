from abc import ABC, abstractmethod
from .writer_interface import Writer
from ..log_levels import LogLevel

class LoggerInterface(ABC):
    """Интерфейс для управления процессом логирования, определяющий основной метод логирования."""

    @abstractmethod
    def set_writer(self, writer: Writer) -> None:
        """
        Устанавливает стратегию записи логов.

        Args:
            writer (Writer): Новая стратегия вывода для записи логов.
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
