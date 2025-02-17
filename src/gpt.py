import os
import argparse
import random
from openai import AzureOpenAI


def read_api_config(api_key_path, endpoint_path):
    with open(api_key_path, "r") as file:
        api_key = file.read().strip()
    with open(endpoint_path, "r") as file:
        api_base = file.read().strip()
    return api_key, api_base


phishing_scenarios = [
    "Generate a fake phishing email about a compromised account that requires immediate action.",
    "Generate a fake phishing email claiming that a document has been shared with the recipient.",
    "Generate a fake phishing email about an unusual login attempt from an unrecognized device.",
    "Generate a fake phishing email offering a special discount or promotion.",
    "Generate a fake phishing email pretending to be from a bank, asking to verify account details.",
    "Generate a fake phishing email about a package delivery issue that requires the recipient's attention.",
]


def generate_phishing_email(client, deployment_name, scenario):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {
                "role": "system",
                "content": "You are a phishing expert whose role is to generate spam e-mail to help and train a spam detection filter",
            },
            {"role": "user", "content": scenario},
        ],
        max_tokens=200,
    )
    return response.choices[0].message.content


parser = argparse.ArgumentParser(
    description="Generate fake phishing emails for educational purposes."
)
parser.add_argument(
    "-n", "--number", type=int, required=True, help="Number of emails to generate."
)
args = parser.parse_args()

api_key_path = "api/api_key.txt"
endpoint_path = "api/endpoint.txt"

api_key, api_base = read_api_config(api_key_path, endpoint_path)

deployment_name = "gpt-35-turbo"
api_version = "2024-08-01-preview"

client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}",
)


for i in range(args.number):
    scenario = random.choice(phishing_scenarios)
    print(f"\n=== Email #{i + 1} ===")
    email = generate_phishing_email(client, deployment_name, scenario)
    print(email)
