# logger/log_strategies.py

from abc import ABC, abstractmethod
from datetime import datetime
import os

class LogStrategy(ABC):
    """Базовый класс стратегии логирования"""

    @abstractmethod
    def log(self, message: str, level: str) -> None:
        pass


class ConsoleLogStrategy(LogStrategy):
    """Стратегия логирования в консоль"""

    def log(self, message: str, level: str) -> None:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} [{level}] {message}")


class FileLogStrategy(LogStrategy):
    """Стратегия логирования в файл"""

    def __init__(self, directory=None):
        # Проверяем, является ли путь папкой
        if directory:
            os.makedirs(directory, exist_ok=True)
            # Генерируем имя файла с меткой времени
            timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
            filename = f"DP.P1.{timestamp}.log"
            self.filepath = os.path.join(directory, filename)
        else:
            # Если путь не указан, используем текущую директорию
            timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
            filename = f"DP.P1.{timestamp}.log"
            self.filepath = os.path.join(os.getcwd(), filename)

    def log(self, message: str, level: str) -> None:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{current_time} [{level}] {message}"
        with open(self.filepath, 'a') as f:
            f.write(log_message + "\n")


class UpperFileLogStrategy(LogStrategy):
    """Стратегия логирования в файл с сообщениями в верхнем регистре"""

    def __init__(self, directory=None):
        # Проверяем, является ли путь папкой
        if directory:
            os.makedirs(directory, exist_ok=True)
            # Генерируем имя файла с меткой времени
            timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
            filename = f"DP.P1.{timestamp}.log"
            self.filepath = os.path.join(directory, filename)
        else:
            # Если путь не указан, используем текущую директорию
            timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
            filename = f"DP.P1.{timestamp}.log"
            self.filepath = os.path.join(os.getcwd(), filename)

    def log(self, message: str, level: str) -> None:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{current_time} [{level}] {message}".upper()
        with open(self.filepath, 'a') as f:
            f.write(log_message + "\n")
