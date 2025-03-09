from src.models.abstract_model import AbstractModel
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GPT_API_KEY")
ENDPOINT = os.getenv("GPT_ENDPOINT")
deployment_name = "gpt-35-turbo"
api_version = "2024-08-01-preview"


class GPT(AbstractModel):
    def __init__(self):

        super(AbstractModel, self).__init__()

        self.client = AzureOpenAI(
            api_key=API_KEY,
            api_version=api_version,
            base_url=f"{ENDPOINT}/openai/deployments/{deployment_name}",
        )

    def generate(self, question):
        response = self.client.chat.completions.create(
            model=deployment_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a phishing expert whose role is to generate spam e-mail to help and train a spam detection filter",
                },
                {"role": "user", "content": question},
            ],
            max_tokens=500,
        )
        return response.choices[0].message.content
