import click
from src.dataset.dataset import SpamDataset
from src.models.gpt_model import GPT
from src.evaluation.evaluate import run_evaluation_suite
from src.models.llm_based_model import LLM
from tqdm import tqdm
import pandas as pd
from src.strategy.zero_shot import ZeroShotStrategy


def write_as_csv(samples, output_filename):
    formatted_samples = []

    for sample in samples:
        formatted_samples.append(
            {
                "Message": sample["text"],
                "Subject": sample["subject"],
                "Spam/Ham": "spam",
                "Date": "2025-03-08",  # @TODO generate random date
            }
        )

    df = pd.DataFrame(formatted_samples)
    df.to_csv(output_filename, index=False)  # index=False to avoid writing row indices


@click.group()
def main():
    pass


@main.command()
@click.option("--n_samples", default=1, help="Number of samples to generate.")
@click.option(
    "--model",
    type=click.Choice(["GPT3", "Phi3"], case_sensitive=False),
    help="Model to use for generating samples.",
)
@click.option("--output", default="out.csv", help="Output file path.")
def generate(n_samples, model, output):
    if model.lower() == "GPT3".lower():
        generator = GPT()
    elif model.lower() == "Phi3".lower():
        generator = LLM()
    else:
        raise Exception(f"Unknown model: {model}")

    dataset = SpamDataset()
    strategy = ZeroShotStrategy(dataset, generator)

    emails = []

    for _ in tqdm(range(n_samples)):
        spam = strategy.generate()
        emails.append(spam)

    print(emails)

    write_as_csv(emails, output)

    print(f"{output} created or overwritten successfully.")


@main.command()
@click.option(
    "--dir",
    type=str,
    help="Path to a directory with CSV file(s) with data to evaluate in Enron format",
)
def evaluate(dir):
    run_evaluation_suite(dir)


if __name__ == "__main__":
    main()
