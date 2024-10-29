from abc import ABC, abstractmethod

class LogOutput(ABC):
    """Абстрактный базовый класс для вывода логов."""

    @abstractmethod
    def write(self, message: str) -> None:
        """Записывает сообщение лога в конкретный вывод."""
        pass
