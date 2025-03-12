"""
Metrics for evaluating the quality of the generated text.
@TODO
"""

from nltk.translate.bleu_score import sentence_bleu
import numpy as np
import copy
import nltk

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
