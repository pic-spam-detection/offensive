from src.models.abstract_model import AbstractModel
from src.dataset.dataset import SpamDataset
from .abstract_strategy import AbstractStrategy
from torch.utils.data import RandomSampler


class FewShotStrategy(AbstractStrategy):
    def __init__(self, dataset: SpamDataset, generator: AbstractModel):
        super().__init__(dataset, generator)

        self.subject_prompt = """
            I want to train a classifier to detect spam emails.
            Please generate {n_to_generate} examples of subject lines of spam emails that are difficult to detect.
            Provide {n_to_generate} subject lines only without any additional text and without "Subject" at the beginning.
            Provide subject lines as a list in JSON format.

            Some examples of subject lines:
            {samples}
        """.strip()

        self.text_prompt = """
            I want to train a classifier to detect spam emails.
            Please generate {n_to_generate} examples of spam emails that are difficult to detect.
            Provide {n_to_generate} bodies of emails only without any additional text.
            Provide these messages as a list in JSON format.

            Some examples of messages:
            {samples}
        """.strip()

    def generate(self, n_samples=5, n_to_generate=1):
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

        subjects = self.generator.generate(
            self.subject_prompt.format(
                samples=subject_samples, n_to_generate=n_to_generate
            )
        )

        texts = self.generator.generate(
            self.text_prompt.format(
                samples=subject_samples, n_to_generate=n_to_generate
            )
        )

        print("subjects", subjects)
        print("texts", texts)

        return {
            "subject": "test",
            "text": "test",
        }
