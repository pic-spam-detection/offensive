from abstract_model import AbstractModel

def generate_spam(model):
  return model.generate()


if __name__ == "__main__":
  model = AbstractModel()

  spam = model.generate()

  print(spam)

