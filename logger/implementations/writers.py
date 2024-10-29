from datetime import datetime
import os
from ..interfaces.writer_interface import Writer

class ConsoleWriter(Writer):
    """Стратегия вывода логов в консоль."""

    def write(self, message: str) -> None:
        print(message)


class FileWriter(Writer):
    """Стратегия вывода логов в файл."""

    def __init__(self, directory=None):
        self.filepath = self._create_log_file(directory)

    def _create_log_file(self, directory):
        """Создает путь для файла логов с учетом директории и времени."""
        timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        filename = f"DP.P1.{timestamp}.log"
        if directory:
            os.makedirs(directory, exist_ok=True)
            return os.path.join(directory, filename)
        return os.path.join(os.getcwd(), filename)

    def write(self, message: str) -> None:
        with open(self.filepath, 'a') as f:
            f.write(message + "\n")


class UpperFileWriter(FileWriter):
    """Стратегия вывода логов в файл, преобразуя текст в верхний регистр."""

    def write(self, message: str) -> None:
        super().write(message.upper())
