import random
from datetime import datetime, timedelta
import pandas as pd
import json
import re


def split_into_batches(total, batch_size):
    if total <= batch_size:
        return [total]

    batches = []

    while total > 0:
        current_batch = min(batch_size, total)
        batches.append(current_batch)
        total -= current_batch

    return batches


def extract_json_list(text):
    print("text", text)
    print("========")

    match = re.search(r"\[.*\]", text, re.DOTALL)

    if match:
        print("match", match)
        print("========")
        json_text = match.group(0)  # Extract the matched JSON text
        email_list = json.loads(json_text)
        print(email_list)
        return email_list
    else:
        print("No valid JSON found!")
        return []


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
                "Message": sample["message"],
                "Subject": sample["subject"],
                "Spam/Ham": "spam",
                "Date": generate_random_date("2020-01-01", "2025-01-01"),
            }
        )

    df = pd.DataFrame(formatted_samples)
    df.to_csv(output_filename, index=False)  # index=False to avoid writing row indices
