import unittest
from unittest.mock import patch, mock_open
from logger import Logger, ConsoleLogOutput, FileLogOutput, UpperFileLogOutput
from logger.log_levels import LogLevel
import re

class TestLogger(unittest.TestCase):

    def setUp(self):
        """Настраивает логгер с консольной стратегией перед каждым тестом."""
        self.console_logger = Logger(strategy=ConsoleLogOutput())

    def _build_expected_message(self, level, message):
        """Формирует регулярное выражение для проверки отформатированного сообщения."""
        return re.compile(rf"\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}}:\d{{2}} \[{level}\] {message}")

    def test_log_info_event_console(self):
        with patch('builtins.print') as mock_print:
            self.console_logger.log_info_event("Test info message")
            expected_message = self._build_expected_message("INFO", "Test info message")
            actual_message = mock_print.call_args[0][0]
            self.assertRegex(actual_message, expected_message)

    def test_log_warning_event_console(self):
        with patch('builtins.print') as mock_print:
            self.console_logger.log_warning_event("Test warning message")
            expected_message = self._build_expected_message("WARN", "Test warning message")
            actual_message = mock_print.call_args[0][0]
            self.assertRegex(actual_message, expected_message)

    def test_log_error_event_console(self):
        with patch('builtins.print') as mock_print:
            self.console_logger.log_error_event("Test error message")
            expected_message = self._build_expected_message("ERROR", "Test error message")
            actual_message = mock_print.call_args[0][0]
            self.assertRegex(actual_message, expected_message)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_log_info_event_file(self, mock_open, mock_makedirs):
        """Тестирование записи сообщения уровня INFO в файл."""
        file_logger = Logger(strategy=FileLogOutput(directory="test_logs"))
        file_logger.log_info_event("Test info message")

        expected_message = self._build_expected_message("INFO", "Test info message")
        actual_message = mock_open().write.call_args[0][0]
        self.assertRegex(actual_message, expected_message)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_log_warning_event_file(self, mock_open, mock_makedirs):
        """Тестирование записи сообщения уровня WARNING в файл."""
        file_logger = Logger(strategy=FileLogOutput(directory="test_logs"))
        file_logger.log_warning_event("Test warning message")

        expected_message = self._build_expected_message("WARN", "Test warning message")
        actual_message = mock_open().write.call_args[0][0]
        self.assertRegex(actual_message, expected_message)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_log_error_event_upper_file(self, mock_open, mock_makedirs):
        """Тестирование записи сообщения уровня ERROR в файл с преобразованием в верхний регистр."""
        upper_file_logger = Logger(strategy=UpperFileLogOutput(directory="test_logs"))
        upper_file_logger.log_error_event("Test error message")

        expected_message = self._build_expected_message("ERROR", "TEST ERROR MESSAGE")
        actual_message = mock_open().write.call_args[0][0]
        self.assertRegex(actual_message, expected_message)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_set_logging_strategy(self, mock_open, mock_makedirs):
        """Тестирование изменения стратегии логирования с консольной на файловую."""
        logger = Logger(strategy=ConsoleLogOutput())
        logger.set_logging_strategy(FileLogOutput(directory="test_logs"))
        logger.log_info_event("Test info message in file")

        expected_message = self._build_expected_message("INFO", "Test info message in file")
        actual_message = mock_open().write.call_args[0][0]
        self.assertRegex(actual_message, expected_message)


if __name__ == '__main__':
    unittest.main()
