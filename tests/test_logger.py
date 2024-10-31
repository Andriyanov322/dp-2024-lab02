import unittest
from unittest.mock import patch, mock_open
from logger import Logger, ConsoleWriter, FileWriter, UpperFileWriter
from logger.log_levels import LogLevel
import re

class TestLogger(unittest.TestCase):

    def setUp(self):
        """Настраивает логгер с консольной стратегией перед каждым тестом."""
        self.console_logger = Logger(writer=ConsoleWriter())

    def _build_expected_message(self, level, message):
        """Формирует отформатированное сообщение для проверки с квадратными скобками вокруг уровня."""
        return f"[{level}] {message}"

    def test_log_info_console(self):
        with patch('builtins.print') as mock_print:
            self.console_logger.log("Test info message", level=LogLevel.INFO)
            expected_message = self._build_expected_message("INFO", "Test info message")
            actual_message = re.sub(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ', '', mock_print.call_args[0][0]).strip()
            self.assertEqual(actual_message, expected_message)

    def test_log_warning_console(self):
        with patch('builtins.print') as mock_print:
            self.console_logger.log("Test warning message", level=LogLevel.WARN)
            expected_message = self._build_expected_message("WARN", "Test warning message")
            actual_message = re.sub(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ', '', mock_print.call_args[0][0]).strip()
            self.assertEqual(actual_message, expected_message)

    def test_log_error_console(self):
        with patch('builtins.print') as mock_print:
            self.console_logger.log("Test error message", level=LogLevel.ERROR)
            expected_message = self._build_expected_message("ERROR", "Test error message")
            actual_message = re.sub(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ', '', mock_print.call_args[0][0]).strip()
            self.assertEqual(actual_message, expected_message)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_log_info_file(self, mock_open, mock_makedirs):
        """Тестирование записи сообщения уровня INFO в файл."""
        file_logger = Logger(writer=FileWriter(directory="test_logs"))
        file_logger.log("Test info message", level=LogLevel.INFO)

        expected_message = self._build_expected_message("INFO", "Test info message")
        actual_message = re.sub(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ', '', mock_open().write.call_args[0][0]).strip()
        self.assertEqual(actual_message, expected_message)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_log_warning_file(self, mock_open, mock_makedirs):
        """Тестирование записи сообщения уровня WARNING в файл."""
        file_logger = Logger(writer=FileWriter(directory="test_logs"))
        file_logger.log("Test warning message", level=LogLevel.WARN)

        expected_message = self._build_expected_message("WARN", "Test warning message")
        actual_message = re.sub(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ', '', mock_open().write.call_args[0][0]).strip()
        self.assertEqual(actual_message, expected_message)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_log_error_upper_file(self, mock_open, mock_makedirs):
        """Тестирование записи сообщения уровня ERROR в файл с преобразованием в верхний регистр."""
        upper_file_logger = Logger(writer=UpperFileWriter(directory="test_logs"))
        msg = 'Test error message'

        upper_file_logger.log(msg, level=LogLevel.ERROR)

        expected_message = self._build_expected_message("ERROR", msg.upper())
        actual_message = re.sub(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ', '', mock_open().write.call_args[0][0]).strip()
        self.assertEqual(actual_message, expected_message)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_set_logging_strategy(self, mock_open, mock_makedirs):
        """Тестирование изменения стратегии логирования с консольной на файловую."""
        logger = Logger(writer=ConsoleWriter())
        logger.set_writer(FileWriter(directory="test_logs"))
        logger.log("Test info message in file", level=LogLevel.INFO)

        expected_message = self._build_expected_message("INFO", "Test info message in file")
        actual_message = re.sub(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} ', '', mock_open().write.call_args[0][0]).strip()
        print(actual_message)
        print(expected_message)
        self.assertEqual(actual_message, expected_message)


if __name__ == '__main__':
    unittest.main()
