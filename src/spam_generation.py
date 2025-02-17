from models.abstract_model import AbstractModel
from models.dataset_sampling_model import DatasetSamplingModel
from models.llm_based_model import LLM
import argparse

MODELS = {
  'llm': LLM,
  'dataset': DatasetSamplingModel,
}


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description="A simple command line spam email generator (for training classifier models)."
  )

  parser.add_argument('--model', type=str, required=True, choices=MODELS.keys(),
                      help='Models available: ' + ', '.join(MODELS.keys()))
  
  parser.add_argument('--n_samples', type=int, required=False, default=5,
                      help='Number of samples to generate')
  
  args = parser.parse_args()

  Model = MODELS[args.model]
  model = Model()

  for n in range(args.n_samples):
    print(f"\n====== Email #{n} ======\n")
    spam = model.generate()
    print(spam)

