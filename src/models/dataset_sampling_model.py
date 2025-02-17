from .abstract_model import AbstractModel
from datasets import load_dataset
import random


class DatasetSamplingModel(AbstractModel):
  def __init__(self):
    super(AbstractModel, self).__init__()
    self.ds = load_dataset("TrainingDataPro/email-spam-classification")

  def __select_random_sample(self):
    random_index = random.randint(0, len(self.ds['train']) - 1)
    return self.ds['train'][random_index]

  def generate(self):
    random_sample = self.__select_random_sample()

    while random_sample['type'] != 'spam':
      random_sample = self.__select_random_sample()

    return f"{random_sample['title']}\n{random_sample['text']}"