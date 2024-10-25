# logger/logger.py

from .singleton import SingletonMeta
from .log_strategies import LogStrategy
from threading import Lock

class Logger(metaclass=SingletonMeta):
    _lock = Lock()

    def __init__(self, strategy: LogStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: LogStrategy) -> None:
        """Устанавливает новую стратегию логирования"""
        self._strategy = strategy

    def log(self, message: str, level="INFO") -> None:
        """Логирует сообщение, используя текущую стратегию"""
        with Logger._lock:
            self._strategy.log(message, level)

    def trace(self, message: str) -> None:
        self.log(message, level="TRACE")

    def info(self, message: str) -> None:
        self.log(message, level="INFO")

    def warn(self, message: str) -> None:
        self.log(message, level="WARN")

    def error(self, message: str) -> None:
        self.log(message, level="ERROR")

    def fatal(self, message: str) -> None:
        self.log(message, level="FATAL")
