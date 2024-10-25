# logger/log_strategies.py

from abc import ABC, abstractmethod
from datetime import datetime
import os

class LogStrategy(ABC):
    """Абстрактный базовый класс для стратегии логирования."""

    @abstractmethod
    def log(self, message: str, level: str) -> None:
        """Определяет метод логирования для конкретной реализации.

        Args:
            message (str): Сообщение для логирования.
            level (str): Уровень логирования, например 'INFO', 'ERROR', и т.д.
        """
        pass

class ConsoleLogStrategy(LogStrategy):
    """Стратегия логирования сообщений в консоль."""

    def log(self, message: str, level: str) -> None:
        """Выводит сообщение с указанием времени и уровня в консоль.

        Args:
            message (str): Сообщение для логирования.
            level (str): Уровень логирования, например 'INFO', 'ERROR', и т.д.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} [{level}] {message}")

class FileLogStrategy(LogStrategy):
    """Стратегия логирования сообщений в файл."""

    def __init__(self, directory=None):
        """Инициализирует FileLogStrategy и создаёт файл для логов.

        Args:
            directory (str, optional): Директория для сохранения файла логов.
                                       Если не указана, файл создаётся в текущей директории.
        """
        if directory:
            os.makedirs(directory, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
            filename = f"DP.P1.{timestamp}.log"
            self.filepath = os.path.join(directory, filename)
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
            filename = f"DP.P1.{timestamp}.log"
            self.filepath = os.path.join(os.getcwd(), filename)

    def log(self, message: str, level: str) -> None:
        """Записывает сообщение с указанием времени и уровня в файл.

        Args:
            message (str): Сообщение для логирования.
            level (str): Уровень логирования, например 'INFO', 'ERROR', и т.д.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{current_time} [{level}] {message}"
        with open(self.filepath, 'a') as f:
            f.write(log_message + "\n")

class UpperFileLogStrategy(LogStrategy):
    """Стратегия логирования сообщений в файл, преобразуя текст в верхний регистр."""

    def __init__(self, directory=None):
        """Инициализирует UpperFileLogStrategy и создаёт файл для логов.

        Args:
            directory (str, optional): Директория для сохранения файла логов.
                                       Если не указана, файл создаётся в текущей директории.
        """
        if directory:
            os.makedirs(directory, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
            filename = f"DP.P1.{timestamp}.log"
            self.filepath = os.path.join(directory, filename)
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
            filename = f"DP.P1.{timestamp}.log"
            self.filepath = os.path.join(os.getcwd(), filename)

    def log(self, message: str, level: str) -> None:
        """Записывает сообщение с указанием времени и уровня в файл, преобразуя текст в верхний регистр.

        Args:
            message (str): Сообщение для логирования.
            level (str): Уровень логирования, например 'INFO', 'ERROR', и т.д.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{current_time} [{level}] {message}".upper()
        with open(self.filepath, 'a') as f:
            f.write(log_message + "\n")
