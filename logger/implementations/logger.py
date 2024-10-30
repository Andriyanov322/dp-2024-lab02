from logger.interfaces.logger_interface import LoggerInterface
from logger.interfaces.writer_interface import Writer
from logger.log_levels import LogLevel
from logger.implementations.singleton import Singleton
from threading import Lock
from datetime import datetime


class Logger(LoggerInterface, Singleton):
    """Класс логгера для записи сообщений с использованием различных уровней логирования и стратегий вывода."""

    _log_lock = Lock()  # Блокировка для записи логов

    def __init__(self, writer: Writer):
        """
        Инициализирует логгер с указанной стратегией записи.

        Args:
            writer (Writer): Стратегия вывода, используемая для записи логов.
        """
        self._writer = writer

    def set_writer(self, writer: Writer) -> None:
        """
        Устанавливает стратегию записи логов.

        Args:
            writer (Writer): Новая стратегия вывода для записи логов.
        """
        self._writer = writer

    def _format_message(self, message: str, level: LogLevel) -> str:
        """
        Форматирует сообщение с указанием времени и уровня логирования.

        Args:
            message (str): Текст сообщения для логирования.
            level (LogLevel): Уровень логирования.

        Returns:
            str: Форматированное сообщение для записи.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{current_time} [{level.value}] {message}"

    def log(self, message: str, level: LogLevel) -> None:
        """
        Логирует сообщение с указанным уровнем.

        Args:
            message (str): Сообщение для записи в лог.
            level (LogLevel): Уровень логирования (например, INFO, ERROR).
        """
        formatted_message = self._format_message(message, level)
        with Logger._log_lock:
            self._writer.write(formatted_message)
