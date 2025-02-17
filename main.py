import click
from src.evaluation.evaluate import run_evaluation_suite
from src.models.llm_based_model import LLM


@click.group()
def main():
    pass


# TODO support different models
@main.command()
@click.option("--n_samples", default=1, help="Number of samples to generate.")
@click.option("--output", default="out.txt", help="Output file path.")
def generate(n_samples, output):
    model = LLM()

    emails = []

    for _ in range(n_samples):
        spam = model.generate()
        emails.append(spam)

    print(emails)

    with open(output, "w") as file:
        file.write("\n".join(emails))

    print(f"{output} created or overwritten successfully.")


# TODO support different models
@main.command()
def evaluate():
    model = LLM()

    run_evaluation_suite(model)


if __name__ == "__main__":
    main()
