from evaluation.visualize import (
    plot_bigrams_frequency,
    plot_word_cloud,
    plot_word_frequency,
)
from nltk.translate.bleu_score import sentence_bleu
import numpy as np
import copy
import nltk
import pandas as pd
import os

nltk.download("punkt")
nltk.download("punkt_tab")


# Adapted from https://www.digitalocean.com/community/tutorials/automated-metrics-for-evaluating-generated-text#self-bleu
def get_bleu_score(sentence, remaining_sentences):
    lst = []
    for i in remaining_sentences:
        bleu = sentence_bleu(sentence, i)
        lst.append(bleu)
    return lst


def get_self_bleu(sentences):
    bleu_scores = []

    for i in sentences:
        sentences_copy = copy.deepcopy(sentences)
        bleu = get_bleu_score(i, sentences_copy)
        bleu_scores.append(bleu)

    return np.mean(bleu_scores)


def run_evaluation_suite(data_dir: str):
    results_dir = "results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        print(f"Directory '{results_dir}' created.")
    else:
        print(f"Directory '{results_dir}' already exists.")

    visual_metrics = {
        "word cloud": plot_word_cloud,
        "word frequency": plot_word_frequency,
        "bigrams frequency": plot_bigrams_frequency,
    }

    for filename in os.listdir(data_dir):
        if filename.endswith(".csv"):
            model_name = filename.replace(".csv", "")

            file_path = os.path.join(data_dir, filename)
            df = pd.read_csv(file_path).dropna()  # @TODO consider only spam emails

            bleu_scores = []
            full_text = ""

            for row in df:
                spam = row["Message"]
                full_text += spam
                sentences = nltk.sent_tokenize(spam)
                bleu_scores.append(get_self_bleu(sentences))

            mean_bleu_score = np.mean(bleu_scores)

            print(f"\nSelf-BLEU: {mean_bleu_score:.3f}")

            for metric, get_metric in visual_metrics.items():
                get_metric(
                    full_text, os.path.join(results_dir, f"{model_name}_{metric}.png")
                )
