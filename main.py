import click
from src.models.model_for_question_answering import ModelForQuestionAnswering
from src.dataset.dataset import SpamDataset
from src.models.gpt_model import GPT
from src.evaluation.report import run_evaluation_suite
from src.models.model_for_casual_lm import ModelForCausalLM
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
            "microsoft/Phi-3.5-mini-instruct",
            "Qwen/Qwen2-1.5B",
            "mistralai/Ministral-8B-Instruct-2410",
            "GSAI-ML/LLaDA-8B-Instruct",
            "Intel/dynamic_tinybert",
        ],
        case_sensitive=True,
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
    if model == "GPT3":
        generator = GPT()
    elif model == "Intel/dynamic_tinybert":
        generator = ModelForQuestionAnswering(model)
    else:
        generator = ModelForCausalLM(model)

    dataset = SpamDataset()

    if strategy == "zero-shot":
        strategy = ZeroShotStrategy(dataset, generator)
    else:
        strategy = FewShotStrategy(dataset, generator)

    emails = strategy.generate(n_to_generate=n_samples)
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
