import click
from src.dataset.dataset import SpamDataset
from src.models.gpt_model import GPT
from src.evaluation.evaluate import run_evaluation_suite
from src.models.llm_based_model import LLM
from tqdm import tqdm
from src.strategy.zero_shot import ZeroShotStrategy


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
@click.option("--output", default="out.txt", help="Output file path.")
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

    with open(output, "w") as file:
        file.write("\n".join(emails))

    print(f"{output} created or overwritten successfully.")


# @TODO run evaluation on files with generated emails rather than on a model directly
@main.command()
@click.option(
    "--path",
    type=str,
    help="Path to CSV file with data in Enron format to evaluate",
)
def evaluate(path):
    run_evaluation_suite(path)


if __name__ == "__main__":
    main()
