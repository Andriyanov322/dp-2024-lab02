import os
from datetime import datetime

class Logger:
    def __init__(self, log_strategy, logs_dir=None):
        self.log_strategy = log_strategy
        self.logs_dir = logs_dir
        if logs_dir:
            os.makedirs(self.logs_dir, exist_ok=True)

    def log(self, message: str) -> None:
        try:
            self.log_strategy.log(message)
        except Exception as e:
            print(f"Error during logging: {e}")

    def info(self, message: str) -> None:
        self.log(f"{self.get_timestamp()} [INFO] {message}")

    def warn(self, message: str) -> None:
        self.log(f"{self.get_timestamp()} [WARN] {message}")

    def error(self, message: str) -> None:
        self.log(f"{self.get_timestamp()} [ERROR] {message}")

    def fatal(self, message: str) -> None:
        self.log(f"{self.get_timestamp()} [FATAL] {message}")

    def get_timestamp(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
