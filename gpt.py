import os
import argparse
from openai import AzureOpenAI

def read_api_config(api_key_path, endpoint_path):
    with open(api_key_path, "r") as file:
        api_key = file.read().strip()
    with open(endpoint_path, "r") as file:
        api_base = file.read().strip()
    return api_key, api_base

def generate_phishing_email(client, deployment_name):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            { "role": "system", "content": "You are a phishing expert whose role is to generate spam e-mail to help and train a spam detection filter" },
            { "role": "user", "content": "Generate a fake phishing/spam email. The email should encourage the recipient to click on a link or download an attachment. You may use social engineering tactics" }
        ],
        max_tokens=200
    )
    return response.choices[0].message.content

parser = argparse.ArgumentParser(description="Generate fake phishing emails for educational purposes.")
parser.add_argument("-n", "--number", type=int, required=True, help="Number of emails to generate.")
args = parser.parse_args()

api_key_path = "api/api_key.txt"
endpoint_path = "api/endpoint.txt"

api_key, api_base = read_api_config(api_key_path, endpoint_path)

deployment_name = 'gpt-35-turbo'
api_version = '2024-08-01-preview'

client = AzureOpenAI(
    api_key=api_key,  
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}"
)


for i in range(args.number):
    print(f"\n=== Email #{i + 1} ===")
    email = generate_phishing_email(client, deployment_name)
    print(email)