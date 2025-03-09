from src.models.abstract_model import AbstractModel
from src.dataset.dataset import SpamDataset
from .abstract_strategy import AbstractStrategy


class ZeroShotStrategy(AbstractStrategy):
    def __init__(self, dataset: SpamDataset, generator: AbstractModel):
        super().__init__(dataset, generator)

        self.prompt = """
            I want to train a classifier to detect spam emails.
            Please generate an example of a spam email that is difficult to detect.
            Provide an email only without any additional text.
        """.strip()

    def generate(self) -> str:
        return self.generator.generate(self.prompt)
