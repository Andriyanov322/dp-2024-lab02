from abc import ABC, abstractmethod

class IWriter(ABC):
    """Абстрактный базовый класс для записи логов."""

    @abstractmethod
    def write(self, message: str) -> None:
        """Записывает сообщение лога в конкретный вывод."""
        pass
