"""Module that contains common functions used in data preparation"""

import re

import numpy as np
import unidecode
from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import LabelEncoder


def text_cleaner(sentences: np.array):
    """Function to clean the text by lowering case,
    removing accents, small words and adittional spaces.
    """

    for index, sentence in enumerate(sentences):
        sentence = sentence.lower()  # lowercase text
        sentence = unidecode.unidecode(sentence)  # remove accents
        sentence = re.sub(r"\W", " ", sentence)  # remove non letters and numbers
        sentence = re.sub(r"\d", " ", sentence)  # remove numbers
        sentence = re.sub(
            r"\b[a-z]{1}\b", " ", sentence, flags=re.I
        )  # remove word size 1
        sentence = re.sub(
            r"\b[a-z]{2}\b", " ", sentence, flags=re.I
        )  # remove word size 2
        sentence = re.sub(
            r"\s+", " ", sentence
        )  # remove adittional space between words
        sentence = re.sub(
            r"^\s+", "", sentence
        )  # remove adittional space in the begining
        sentence = re.sub(r"\s+$", "", sentence)  # remove adittional space in the end
        sentences[index] = sentence

    return sentences


def label_encoder(x):
    """Function to encoder a variable from string to integer (0,1,2...)."""
    encoder = LabelEncoder()
    x_encoded = encoder.fit_transform(x)
    return x_encoded, encoder


def random_under_sampler(X, y, max_num_samples_per_class, random_state=0):
    """Function to randomly under sample."""

    labels, counts = np.unique(y, return_inverse=False, return_counts=True)
    label_counts = dict(
        zip(
            range(len(labels)),
            [min(max_num_samples_per_class, count) for count in counts.tolist()],
        )
    )
    rus = RandomUnderSampler(sampling_strategy=label_counts, random_state=random_state)

    X_resampled, y_resampled = rus.fit_resample(X.reshape(-1, 1), y)
    return (
        X_resampled.reshape(
            -1,
        ),
        y_resampled,
    )
