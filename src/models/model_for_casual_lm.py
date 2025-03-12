from .abstract_model import AbstractModel
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from dotenv import load_dotenv
import os

load_dotenv()


class ModelForCausalLM(AbstractModel):
    def __init__(self, llm_name):

        super(AbstractModel, self).__init__()

        hf_token = os.getenv("HF_TOKEN")

        model = AutoModelForCausalLM.from_pretrained(
            llm_name,
            device_map="cuda",
            torch_dtype="auto",
            trust_remote_code=True,
            token=hf_token,
        )

        tokenizer = AutoTokenizer.from_pretrained(llm_name, token=hf_token)

        self.pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
        )

    def __parse_output(self, output):
        return output[0]["generated_text"]

    def generate(self, question):
        generation_args = {
            "max_new_tokens": 500,
            "return_full_text": False,
            "temperature": 0.9,
            "do_sample": True,
        }

        messages = [
            {
                "role": "system",
                "content": "You are a phishing expert whose role is to generate spam e-mail to help and train a spam detection filter",
            },
            {
                "role": "user",
                "content": question,
            },
        ]

        output = self.pipe(messages, **generation_args)
        return self.__parse_output(output)
