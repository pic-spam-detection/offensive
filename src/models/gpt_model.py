from abstract_model import AbstractModel
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GPT_API_KEY")

deployment_name = "gpt-35-turbo"
api_version = "2024-08-01-preview"


class GPT(AbstractModel):
    def __init__(self):

        super(AbstractModel, self).__init__()

        self.client = AzureOpenAI(
            api_key=API_KEY,
            api_version=api_version,
            base_url=f"{API_KEY}/openai/deployments/{deployment_name}",
        )

    def generate(
        self,
        question="I want to train a classifier to detect spam emails. Please generate an example of a spam email that is difficult to detect. Provide an email only without any additional text.",
    ):
        response = self.client.chat.completions.create(
            model=deployment_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a phishing expert whose role is to generate spam e-mail to help and train a spam detection filter",
                },
                {"role": "user", "content": question},
            ],
            max_tokens=200,
        )
        return response.choices[0].message.content
