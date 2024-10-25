# main.py

from logger import Logger, ConsoleLogStrategy, FileLogStrategy, UpperFileLogStrategy

if __name__ == "__main__":
    # Инициализация логгера с консольной стратегией
    logger = Logger(strategy=ConsoleLogStrategy())
    logger.info("This is an info message in console.")
    logger.warn("This is a warning message in console.")
    logger.error("This is an error message in console.")

    # Задаем папку для файла лога
    log_directory = "logs"

    # Переключаем стратегию на запись в файл, файл создается автоматически внутри logs
    logger.set_strategy(FileLogStrategy(directory=log_directory))
    logger.warn("This is a warning message in file.")
    logger.info("This is an info message in file.")
    logger.error("This is an error message in file.")

    log_directory = "logs/logi"

    # Переключаем стратегию на запись в файл с верхним регистром в папке logs
    logger.set_strategy(UpperFileLogStrategy(directory=log_directory))
    logger.error("This is an error message in uppercase file.")
    logger.warn("This is a warning message in uppercase file.")
    logger.info("This is an info message in uppercase file.")
