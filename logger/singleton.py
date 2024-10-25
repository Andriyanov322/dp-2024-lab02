# logger/singleton.py

import threading


class SingletonMeta(type):
    """Мета-класс Singleton, обеспечивающий существование только одного экземпляра класса."""

    _instances = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """Создаёт или возвращает уже существующий экземпляр класса.

        Args:
            *args: Позиционные аргументы конструктора.
            **kwargs: Именованные аргументы конструктора.

        Returns:
            instance: Существующий или новый экземпляр класса.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
