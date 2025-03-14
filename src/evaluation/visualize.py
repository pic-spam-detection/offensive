"""
Visualizations for the generated text.
"""

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns
import re


def plot_word_cloud(texts, save_filepath):
    full_text = " ".join(texts)

    wordcloud = WordCloud(
        width=3000,
        height=2000,
        random_state=1,
        background_color="white",
        collocations=False,
        stopwords=STOPWORDS,
    ).generate(full_text)

    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(save_filepath, bbox_inches="tight")
    plt.clf()


def plot_word_frequency(texts, save_filepath):
    full_text = " ".join(texts)

    cleaned_text = re.sub(r"[-/]", " ", full_text)  # Replace '-' and '/' with space
    words = cleaned_text.lower().split()
    word_counts = Counter(words)

    word_freq = pd.DataFrame(
        word_counts.items(), columns=["Word", "Frequency"]
    ).sort_values(by="Frequency", ascending=False)

    word_freq.head(10).plot(kind="bar", x="Word", y="Frequency", legend=False)
    plt.title("Top Words Frequency")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.savefig(save_filepath, bbox_inches="tight")
    plt.clf()


def plot_bigrams_frequency(texts, save_filepath):
    vectorizer = CountVectorizer(ngram_range=(2, 2))
    X = vectorizer.fit_transform(texts)
    bigram_counts = X.toarray().sum(axis=0)

    bigrams_df = pd.DataFrame(
        bigram_counts, index=vectorizer.get_feature_names_out(), columns=["Frequency"]
    )
    bigrams_df = bigrams_df.sort_values(by="Frequency", ascending=False)

    sns.barplot(x=bigrams_df.index[:10], y=bigrams_df.Frequency[:10])
    plt.title("Top Bigrams Frequency")
    plt.xticks(rotation=45)
    plt.ylabel("Frequency")
    plt.savefig(save_filepath, bbox_inches="tight")
    plt.clf()
