from .logging_strategies import LogOutput
from .logger_interface import LogManager
from .log_levels import LogLevel
from threading import Lock
from datetime import datetime

class Logger(LogManager):
    """Класс логгера, реализующий интерфейс LogManager и паттерн Singleton для логирования сообщений."""
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        """Реализация Singleton с использованием метода __new__."""
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, strategy: LogOutput):
        self._strategy = strategy

    def set_logging_strategy(self, strategy: LogOutput) -> None:
        """Устанавливает стратегию логирования."""
        self._strategy = strategy

    def _format_message(self, message: str, level: LogLevel) -> str:
        """Форматирует сообщение с учетом уровня логирования и времени."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{current_time} [{level.value}] {message}"

    def _log_event(self, message: str, level: LogLevel) -> None:
        """Приватный метод для логирования события с заданным уровнем."""
        formatted_message = self._format_message(message, level)
        with Logger._lock:
            self._strategy.write(formatted_message)

    def log_event(self, message: str, level: LogLevel) -> None:
        """Реализует метод log_event, определенный в интерфейсе LogManager."""
        self._log_event(message, level)

    def log_trace_event(self, message: str) -> None:
        """Логирует событие уровня TRACE."""
        self._log_event(message, level=LogLevel.TRACE)

    def log_info_event(self, message: str) -> None:
        """Логирует событие уровня INFO."""
        self._log_event(message, level=LogLevel.INFO)

    def log_warning_event(self, message: str) -> None:
        """Логирует событие уровня WARNING."""
        self._log_event(message, level=LogLevel.WARN)

    def log_error_event(self, message: str) -> None:
        """Логирует событие уровня ERROR."""
        self._log_event(message, level=LogLevel.ERROR)

    def log_fatal_event(self, message: str) -> None:
        """Логирует событие уровня FATAL."""
        self._log_event(message, level=LogLevel.FATAL)
