from logger import Logger, ConsoleLogOutput, FileLogOutput, UpperFileLogOutput
from logger.log_levels import LogLevel

if __name__ == "__main__":
    # Инициализация логгера с консольной стратегией
    logger = Logger(strategy=ConsoleLogOutput())
    logger.log_info_event("This is an info message in console.")
    logger.log_warning_event("This is a warning message in console.")
    logger.log_error_event("This is an error message in console.")

    # Задаем папку для файла лога
    log_directory = "logs"

    # Переключаем стратегию на запись в файл
    logger.set_logging_strategy(FileLogOutput(directory=log_directory))
    logger.log_warning_event("This is a warning message in file.")
    logger.log_info_event("This is an info message in file.")
    logger.log_error_event("This is an error message in file.")

    log_directory = "logs/logi"

    # Переключаем стратегию на запись в файл с верхним регистром в папке logs
    logger.set_logging_strategy(UpperFileLogOutput(directory=log_directory))
    logger.log_error_event("This is an error message in uppercase file.")
    logger.log_warning_event("This is a warning message in uppercase file.")
    logger.log_info_event("This is an info message in uppercase file.")
