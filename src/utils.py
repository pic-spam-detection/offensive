import random
from datetime import datetime, timedelta
import pandas as pd


def generate_random_date(start_date: str, end_date: str) -> str:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    delta = end - start
    random_days = random.randint(0, delta.days)
    random_date = start + timedelta(days=random_days)

    return random_date.strftime("%Y-%m-%d")


def write_as_csv(generated_samples, output_filename):
    formatted_samples = []

    for sample in generated_samples:
        formatted_samples.append(
            {
                "Message": sample["text"],
                "Subject": sample["subject"],
                "Spam/Ham": "spam",
                "Date": generate_random_date("2020-01-01", "2025-01-01"),
            }
        )

    df = pd.DataFrame(formatted_samples)
    df.to_csv(output_filename, index=False)  # index=False to avoid writing row indices
