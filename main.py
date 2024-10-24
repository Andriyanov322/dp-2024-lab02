from logger import Logger
from logger.log_strategies import ConsoleLogStrategy, FileLogStrategy, UpperCaseFileLogStrategy
import os

def main():
    # Директория для логов
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)

    # Пример логирования в консоль
    console_logger = Logger(ConsoleLogStrategy())
    console_logger.info("This is an info message logged to console.")
    console_logger.warn("This is a warning message in console.")
    console_logger.error("This is an error message logged to console.")

    # Пример логирования в файл
    file_logger = Logger(FileLogStrategy(logs_dir))
    file_logger.info("This is an info message logged to file.")
    file_logger.warn("This is a warning message logged to file.")
    file_logger.error("This is an error message logged to file.")

    # Пример логирования в файл с верхним регистром
    upper_case_logger = Logger(UpperCaseFileLogStrategy(logs_dir))
    upper_case_logger.info("This message will be logged in uppercase.")
    upper_case_logger.warn("This warning will be logged in uppercase.")
    upper_case_logger.error("This error will be logged in uppercase.")

    try:
        # Искусственно вызванная ошибка для демонстрации
        result = 10 / 0
    except ZeroDivisionError as e:
        console_logger.error(f"Caught an exception: {e}")
        file_logger.error(f"Caught an exception: {e}")
        upper_case_logger.error(f"Caught an exception: {e}")

    console_logger.info("Application is shutting down.")

if __name__ == "__main__":
    main()
