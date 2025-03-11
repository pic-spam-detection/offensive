import click
from src.dataset.dataset import SpamDataset
from src.models.gpt_model import GPT
from src.evaluation.report import run_evaluation_suite
from src.models.llm_based_model import LLM
from tqdm import tqdm
import pandas as pd
from src.strategy.zero_shot import ZeroShotStrategy
from src.strategy.few_shot import FewShotStrategy
from src.utils import write_as_csv


@click.group()
def main():
    pass


@main.command()
@click.option("--n_samples", default=1, help="Number of samples to generate.")
@click.option(
    "--model",
    type=click.Choice(
        [
            "GPT3",
            "microsoft/Phi-3.5",
            "mistralai/Ministral-8B",
            "meta-llama/Llama-3.1-8B",
        ],
        case_sensitive=False,
    ),
    help="Model to use for generating samples.",
)
@click.option("--output", default="out.csv", help="Output file path.")
@click.option(
    "--strategy",
    type=click.Choice(
        [
            "zero-shot",
            "few-shot",
        ],
        case_sensitive=True,
    ),
    help="Strategy to use.",
)
def generate(n_samples, model, output, strategy):
    if model.lower() == "GPT3".lower():
        generator = GPT()
    elif model.lower() == "microsoft/Phi-3.5".lower():
        generator = LLM("microsoft/Phi-3.5-mini-instruct")
    elif model.lower() == "mistralai/Ministral-8B".lower():
        generator = LLM("mistralai/Ministral-8B-Instruct-2410")
    elif model.lower() == "meta-llama/Llama-3.1-8B".lower():
        generator = LLM("meta-llama/Llama-3.1-8B-Instruct")
    else:
        raise Exception(f"Unknown model: {model}")

    dataset = SpamDataset()

    if strategy == "zero-shot":
        strategy = ZeroShotStrategy(dataset, generator)
    else:
        strategy = FewShotStrategy(dataset, generator)

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
