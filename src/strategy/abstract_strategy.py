from abc import ABC, abstractmethod

from abstract_model import AbstractModel
from dataset.dataset import SpamDataset


class AbstractStrategy(ABC):
    def __init__(self, dataset: SpamDataset, generator: AbstractModel):
        self.generator = generator
        self.dataset = dataset

    @abstractmethod
    def generate(self) -> str:
        return "spam"
