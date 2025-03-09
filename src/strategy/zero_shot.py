from src.models.abstract_model import AbstractModel
from src.dataset.dataset import SpamDataset
from .abstract_strategy import AbstractStrategy


class ZeroShotStrategy(AbstractStrategy):
    def __init__(self, dataset: SpamDataset, generator: AbstractModel):
        super().__init__(dataset, generator)

        self.subject_prompt = """
            I want to train a classifier to detect spam emails.
            Please generate an example of a subject line of spam email that is difficult to detect.
            Provide a subject line only without any additional text.
        """.strip()

        self.text_prompt = """
            I want to train a classifier to detect spam emails.
            Please generate an example of a spam email that is difficult to detect.
            Provide a body of the email only without any additional text.
        """.strip()

    # @TODO enforce types
    def generate(self):
        return {
            "subject": self.generator.generate(self.subject_prompt),
            "text": self.generator.generate(self.text_prompt),
        }
