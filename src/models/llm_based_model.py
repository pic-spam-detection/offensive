from .abstract_model import AbstractModel
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


class LLM(AbstractModel):
    def __init__(self):

        super(AbstractModel, self).__init__()

        model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Phi-3.5-mini-instruct",
            device_map="cuda",
            torch_dtype="auto",
            trust_remote_code=True,
        )

        tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3.5-mini-instruct")

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
                "role": "user",
                "content": question,
            },
        ]

        output = self.pipe(messages, **generation_args)
        return self.__parse_output(output)
