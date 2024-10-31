from logger.implementations.logger import Logger
from logger.implementations.writers import ConsoleWriter, FileWriter, UpperFileWriter
from logger.log_levels import LogLevel

if __name__ == "__main__":
    # Инициализация логгера с консольной стратегией
    logger = Logger(writer=ConsoleWriter())
    logger.log("This is an info message in console.", level=LogLevel.INFO)
    logger.log("This is a warning message in console.", level=LogLevel.WARN)
    logger.log("This is an error message in console.", level=LogLevel.ERROR)

    # Задаем папку для файла лога
    log_directory = "logs"

    # Переключаем стратегию на запись в файл
    logger.set_writer(FileWriter(directory=log_directory))
    logger.log("This is a warning message in file.", level=LogLevel.WARN)
    logger.log("This is an info message in file.", level=LogLevel.INFO)
    logger.log("This is an error message in file.", level=LogLevel.ERROR)

    log_directory = "logs/logi"

    # Переключаем стратегию на запись в файл с верхним регистром
    logger.set_writer(UpperFileWriter(directory=log_directory))
    logger.log("This is an error message in uppercase file.", level=LogLevel.ERROR)
    logger.log("This is a warning message in uppercase file.", level=LogLevel.WARN)
    logger.log("This is an info message in uppercase file.", level=LogLevel.INFO)
