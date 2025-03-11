"""
A script for creating automatic evaluation report for the generated text obtained from different models.
"""

from src.evaluation.evaluate import get_self_bleu
from src.evaluation.visualize import (
    plot_bigrams_frequency,
    plot_word_cloud,
    plot_word_frequency,
)
import numpy as np
import nltk
import pandas as pd
import os


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
            texts = df["Message"].to_numpy()

            for index, row in df.iterrows():
                spam = row["Message"]
                sentences = nltk.sent_tokenize(spam)
                bleu_scores.append(get_self_bleu(sentences))

            mean_bleu_score = np.mean(bleu_scores)

            print(f"\nSelf-BLEU: {mean_bleu_score:.3f}")

            for metric, get_metric in visual_metrics.items():
                get_metric(
                    texts, os.path.join(results_dir, f"{model_name}_{metric}.png")
                )
