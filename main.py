from logger import Logger, ConsoleWriter, FileWriter, UpperFileWriter, LogLevel

if __name__ == "__main__":
    # Инициализация логгера с консольной стратегией
    logger = Logger(writer=ConsoleWriter())
    logger.log_info("This is an info message in console.")
    logger.log_warning("This is a warning message in console.")
    logger.log_error("This is an error message in console.")

    # Задаем папку для файла лога
    log_directory = "logs"

    # Переключаем стратегию на запись в файл
    logger.set_writer(FileWriter(directory=log_directory))
    logger.log_warning("This is a warning message in file.")
    logger.log_info("This is an info message in file.")
    logger.log_error("This is an error message in file.")

    log_directory = "logs/logi"

    # Переключаем стратегию на запись в файл с верхним регистром в папке logs
    logger.set_writer(UpperFileWriter(directory=log_directory))
    logger.log_error("This is an error message in uppercase file.")
    logger.log_warning("This is a warning message in uppercase file.")
    logger.log_info("This is an info message in uppercase file.")
