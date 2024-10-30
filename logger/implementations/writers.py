from datetime import datetime
import os
from logger.interfaces.writer_interface import Writer

class ConsoleWriter(Writer):
    """Стратегия вывода логов в консоль."""

    def write(self, message: str) -> None:
        """
        Выводит сообщение в консоль.

        Args:
            message (str): Сообщение для вывода.
        """
        print(message)


class FileWriter(Writer):
    """Стратегия вывода логов в файл."""

    def __init__(self, directory: str = None):
        """
        Инициализирует файловую стратегию с указанием директории для сохранения логов.

        Args:
            directory (str, optional): Путь к директории для хранения лог-файлов.
                                       Если None, используются текущая рабочая директория.
        """
        self.filepath = self._create_log_file(directory)

    def _create_log_file(self, directory: str) -> str:
        """
        Создает путь для лог-файла с именем на основе текущей даты и времени.

        Args:
            directory (str): Путь к директории для хранения лог-файла.

        Returns:
            str: Полный путь к создаваемому лог-файлу.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        filename = f"DP.P1.{timestamp}.log"
        if directory:
            os.makedirs(directory, exist_ok=True)
            return os.path.join(directory, filename)
        return os.path.join(os.getcwd(), filename)

    def write(self, message: str) -> None:
        """
        Записывает сообщение в файл.

        Args:
            message (str): Сообщение для записи в файл.
        """
        with open(self.filepath, 'a') as f:
            f.write(message + "\n")


class UpperFileWriter(FileWriter):
    """Стратегия вывода логов в файл, преобразуя текст в верхний регистр."""

    def write(self, message: str) -> None:
        """
        Записывает сообщение в файл в верхнем регистре.

        Args:
            message (str): Сообщение для записи в файл, преобразованное в верхний регистр.
        """
        super().write(message.upper())
