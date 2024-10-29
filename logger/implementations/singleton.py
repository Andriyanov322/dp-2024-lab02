from threading import Lock

class Singleton:
    """Базовый класс Singleton, обеспечивающий создание единственного экземпляра."""
    _instances = {}
    _instance_lock = Lock()

    def __new__(cls, *args, **kwargs):
        """Создает единственный экземпляр класса с использованием блокировки."""
        if cls not in cls._instances:
            with cls._instance_lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]
