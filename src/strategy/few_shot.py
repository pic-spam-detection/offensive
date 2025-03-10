from src.models.abstract_model import AbstractModel
from src.dataset.dataset import SpamDataset
from .abstract_strategy import AbstractStrategy
from torch.utils.data import RandomSampler


class FewShotStrategy(AbstractStrategy):
    def __init__(self, dataset: SpamDataset, generator: AbstractModel):
        super().__init__(dataset, generator)

        self.subject_prompt = """
            I want to train a classifier to detect spam emails.
            Please generate an example of a subject line of spam email that is difficult to detect.
            Provide a subject line only without any additional text and without "Subject" at the beginning.

            Some examples:
            {samples}
        """.strip()

        self.text_prompt = """
            I want to train a classifier to detect spam emails.
            Please generate an example of a spam email that is difficult to detect.
            Provide a body of the email only without any additional text.

            Some email examples:
            {samples}
        """.strip()

    def generate(self, n_samples=5):
        subject_samples = ""
        text_samples = ""

        for _ in range(n_samples):
            random_sample = RandomSampler(
                self.dataset, num_samples=n_samples, replacement=False
            )
            text_samples += random_sample["text"]
            text_samples += "\n\n"

            subject_samples += random_sample["subject"]
            subject_samples += "\n\n"

        return {
            "subject": self.generator.generate(
                self.subject_prompt.format(samples=subject_samples)
            ),
            "text": self.generator.generate(
                self.text_prompt.format(samples=text_samples)
            ),
        }
