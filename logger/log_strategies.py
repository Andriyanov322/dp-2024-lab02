import os
from abc import ABC, abstractmethod
from datetime import datetime

class LogStrategy(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        """Метод для логирования сообщения."""
        pass

class ConsoleLogStrategy(LogStrategy):
    def log(self, message: str) -> None:
        print(message)

class FileLogStrategy(LogStrategy):
    def __init__(self, logs_dir: str) -> None:
        self.logs_dir = logs_dir
        timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        self.filepath = os.path.join(os.getcwd(), logs_dir, f"DP.P1.{timestamp}.log")

    def log(self, message: str) -> None:
        try:
            with open(self.filepath, 'a') as f:
                f.write(message + "\n")
        except Exception as e:
            print(f"Error logging to file: {e}")

class UpperCaseFileLogStrategy(LogStrategy):
    def __init__(self, logs_dir: str) -> None:
        self.logs_dir = logs_dir
        timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        self.filepath = os.path.join(logs_dir, f"DP.P1.{timestamp}.log")

    def log(self, message: str) -> None:
        try:
            with open(self.filepath, 'a') as f:
                f.write(message.upper() + "\n")
        except Exception as e:
            print(f"Error logging to file: {e}")
