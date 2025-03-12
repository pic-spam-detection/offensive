from .abstract_model import AbstractModel
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from dotenv import load_dotenv
import os
import torch

load_dotenv()


class ModelForQuestionAnswering(AbstractModel):
    def __init__(self, llm_name):

        super(AbstractModel, self).__init__()

        hf_token = os.getenv("HF_TOKEN")

        self.tokenizer = AutoTokenizer.from_pretrained(llm_name)
        self.model = AutoModelForQuestionAnswering.from_pretrained(llm_name)

    def generate(self, question):
        # generation_args = {
        #     "max_new_tokens": 500,
        #     "return_full_text": False,
        #     "temperature": 0.9,
        #     "do_sample": True,
        # }

        context = "You are a phishing expert whose role is to generate spam e-mail to help and train a spam detection filter"

        tokens = self.tokenizer.encode_plus(
            question, context, return_tensors="pt", truncation=True
        )

        input_ids = tokens["input_ids"]
        attention_mask = tokens["attention_mask"]

        outputs = self.model(input_ids, attention_mask=attention_mask)
        start_scores = outputs.start_logits
        end_scores = outputs.end_logits

        # Find the start and end positions of the answer
        answer_start = torch.argmax(start_scores)
        answer_end = torch.argmax(end_scores) + 1
        answer = self.tokenizer.convert_tokens_to_string(
            self.tokenizer.convert_ids_to_tokens(input_ids[0][answer_start:answer_end])
        )

        print("answer", answer)

        return answer
