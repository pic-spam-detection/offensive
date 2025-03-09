from abc import ABC, abstractmethod


class AbstractModel(ABC):
    @abstractmethod
    def generate(self, question):
        return "answer"
