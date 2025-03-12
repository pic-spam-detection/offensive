from src.models.abstract_model import AbstractModel
from src.dataset.dataset import SpamDataset
from src.utils import extract_json_list, split_into_batches
from .abstract_strategy import AbstractStrategy
from torch.utils.data import DataLoader, RandomSampler


class FewShotStrategy(AbstractStrategy):
    def __init__(self, dataset: SpamDataset, generator: AbstractModel):
        super().__init__(dataset, generator)

        self.subject_prompt = """
            I want to train a classifier to detect spam emails.
            Please generate {n_to_generate} examples of subject lines of spam emails that are difficult to detect.
            Provide {n_to_generate} subject lines only without any additional text.
            Provide subject lines as a list in JSON format.

            Some examples of subject lines:
            {samples}

            Provide a simple JSON list only without any additional text or explanations. Do not add "Subject" at the beginning. For example: ['test', 'title2'].
        """.strip()

        self.text_prompt = """
            I want to train a classifier to detect spam emails.
            Please generate {n_to_generate} examples of spam emails that are difficult to detect.
            Provide {n_to_generate} bodies of emails only without any additional text.
            Provide these messages as a list in JSON format.

            Some examples of messages:
            {samples}

            Provide a simple JSON list only without any additional text or explanations. For example: ['test', 'title2'].
        """.strip()

    def generate(self, n_samples=5, n_to_generate=1, batch_size=10):
        subjects = []
        texts = []

        for batch in split_into_batches(n_to_generate, batch_size):
            subject_samples = ""
            text_samples = ""

            random_sampler = RandomSampler(
                self.dataset, num_samples=n_samples, replacement=False
            )
            random_data_loader = DataLoader(self.dataset, sampler=random_sampler)

            for random_sample in random_data_loader:
                text_samples += random_sample["message"][0]
                text_samples += "\n\n"

                subject_samples += random_sample["subject"][0]
                subject_samples += "\n\n"

            new_subjects = self.generator.generate(
                self.subject_prompt.format(samples=subject_samples, n_to_generate=batch)
            )

            new_texts = self.generator.generate(
                self.text_prompt.format(samples=subject_samples, n_to_generate=batch)
            )

            subjects.extend(extract_json_list(new_subjects))
            texts.extend(extract_json_list(new_texts))

        print("subjects", subjects)
        print("texts", texts)

        return [
            {"subject": subject, "message": text}
            for subject, text in zip(subjects, texts)
        ]
