from src.models.abstract_model import AbstractModel
from src.dataset.dataset import SpamDataset
from .abstract_strategy import AbstractStrategy
from torch.utils.data import RandomSampler


class FewShotStrategy(AbstractStrategy):
    def __init__(self, dataset: SpamDataset, generator: AbstractModel):
        super().__init__(dataset, generator)

        self.prompt_template = """
            I want to train a classifier to detect spam emails.
            Please generate an example of a spam email that is difficult to detect.
            Provide an email only without any additional text.

            Some email examples:
            {samples}
        """.strip()

    def generate(self, n_samples=5) -> str:
        samples = ""

        for _ in range(n_samples):
            random_sample = RandomSampler(
                self.dataset, num_samples=n_samples, replacement=False
            )
            samples += random_sample["text"]
            samples += "\n\n"

        return self.generator.generate(self.prompt_template.format(samples=samples))
