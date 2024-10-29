from ..interfaces.logger_interface import LoggerInterface
from ..interfaces.writer_interface import Writer
from ..log_levels import LogLevel
from .singleton import Singleton
from threading import Lock
from datetime import datetime

class Logger(LoggerInterface, Singleton):
    """Класс логгера, реализующий интерфейс LoggerInterface для логирования сообщений."""
    _log_lock = Lock()

    def __init__(self, writer: Writer):
        self._writer = writer

    def set_writer(self, writer: Writer) -> None:
        """Устанавливает стратегию записи логов."""
        self._writer = writer

    def _format_message(self, message: str, level: LogLevel) -> str:
        """Форматирует сообщение с учетом уровня логирования и времени."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{current_time} [{level.value}] {message}"

    def _log(self, message: str, level: LogLevel) -> None:
        """Приватный метод для логирования события с заданным уровнем."""
        formatted_message = self._format_message(message, level)
        with Logger._log_lock:
            self._writer.write(formatted_message)

    def log(self, message: str, level: LogLevel) -> None:
        """Логирует сообщение с заданным уровнем."""
        self._log(message, level)

    def log_trace(self, message: str) -> None:
        """Логирует сообщение уровня TRACE."""
        self._log(message, level=LogLevel.TRACE)

    def log_info(self, message: str) -> None:
        """Логирует сообщение уровня INFO."""
        self._log(message, level=LogLevel.INFO)

    def log_warning(self, message: str) -> None:
        """Логирует сообщение уровня WARNING."""
        self._log(message, level=LogLevel.WARN)

    def log_error(self, message: str) -> None:
        """Логирует сообщение уровня ERROR."""
        self._log(message, level=LogLevel.ERROR)

    def log_fatal(self, message: str) -> None:
        """Логирует сообщение уровня FATAL."""
        self._log(message, level=LogLevel.FATAL)
