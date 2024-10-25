# tests/test_logger.py

import os
import unittest
from unittest.mock import patch
from io import StringIO
from logger import Logger, ConsoleLogStrategy, FileLogStrategy, UpperFileLogStrategy


class TestLogger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Папка для тестовых логов
        cls.log_directory = "logs"
        os.makedirs(cls.log_directory, exist_ok=True)

    def setUp(self):
        """Настройка логгера перед каждым тестом."""
        # Инициализация логгера с консольной стратегией по умолчанию
        self.logger = Logger(ConsoleLogStrategy())

    def test_singleton_instance(self):
        """Тест, что Logger является синглтоном."""
        logger1 = Logger(ConsoleLogStrategy())
        logger2 = Logger(ConsoleLogStrategy())
        self.assertIs(logger1, logger2, "Logger не является синглтоном!")

    @patch('sys.stdout', new_callable=StringIO)
    def test_console_log_strategy(self, mock_stdout):
        """Тестирование стратегии логирования в консоль."""
        self.logger.set_strategy(ConsoleLogStrategy())

        # Логируем сообщения
        self.logger.info("This is an info message in console.")
        self.logger.warn("This is a warning message in console.")
        self.logger.error("This is an error message in console.")

        # Получаем захваченный вывод
        output = mock_stdout.getvalue()

        # Проверка наличия нужных сообщений
        self.assertIn("[INFO] This is an info message in console.", output)
        self.assertIn("[WARN] This is a warning message in console.", output)
        self.assertIn("[ERROR] This is an error message in console.", output)

    def test_file_log_strategy(self):
        """Тестирование стратегии логирования в файл."""
        file_strategy = FileLogStrategy(directory=self.log_directory)
        self.logger.set_strategy(file_strategy)

        # Логируем сообщения
        self.logger.info("This is an info message in file.")
        self.logger.warn("This is a warning message in file.")
        self.logger.error("This is an error message in file.")

        # Проверка, что файл был создан
        log_files = os.listdir(self.log_directory)
        self.assertGreater(len(log_files), 0, "Файл для логов не был создан")

        # Проверяем содержимое последнего созданного файла
        log_file_path = os.path.join(self.log_directory, log_files[-1])
        with open(log_file_path, 'r') as f:
            logs = f.read()
            self.assertIn("[INFO] This is an info message in file.", logs)
            self.assertIn("[WARN] This is a warning message in file.", logs)
            self.assertIn("[ERROR] This is an error message in file.", logs)

    def test_upper_file_log_strategy(self):
        """Тестирование стратегии логирования в файл с верхним регистром."""
        upper_file_strategy = UpperFileLogStrategy(directory=self.log_directory)
        self.logger.set_strategy(upper_file_strategy)

        # Логируем сообщения
        self.logger.info("This is an info message in UPPER file.")
        self.logger.warn("This is a warning message in UPPER file.")
        self.logger.error("This is an error message in UPPER file.")

        # Проверяем, что файл был создан
        log_files = os.listdir(self.log_directory)
        self.assertGreater(len(log_files), 0, "Файл для логов в верхнем регистре не был создан")

        # Проверяем содержимое последнего созданного файла
        log_file_path = os.path.join(self.log_directory, log_files[-1])
        with open(log_file_path, 'r') as f:
            logs = f.read()
            self.assertIn("[INFO] THIS IS AN INFO MESSAGE IN UPPER FILE.", logs)
            self.assertIn("[WARN] THIS IS A WARNING MESSAGE IN UPPER FILE.", logs)
            self.assertIn("[ERROR] THIS IS AN ERROR MESSAGE IN UPPER FILE.", logs)

    @classmethod
    def tearDownClass(cls):
        """Удаляем созданные файлы и папку после завершения тестов."""
        for log_file in os.listdir(cls.log_directory):
            file_path = os.path.join(cls.log_directory, log_file)
            os.remove(file_path)
        os.rmdir(cls.log_directory)


if __name__ == "__main__":
    unittest.main()
