"""
This is a boilerplate pipeline
generated using Kedro 0.18.12
"""

import json
import logging
import pickle
from typing import Any, Dict

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier

from ml_based_text_classification.utils.data_prep import (
    label_encoder,
    random_under_sampler,
    text_cleaner,
)
from ml_based_text_classification.utils.model_evaluation import (
    classifier_metrics_report_generator,
)


def prepare_data(
    data: pd.DataFrame,
    parameters: Dict[str, Any],
):
    """Prepare the data for model training and evaluation."""

    # Unpack parameters
    test_size = parameters["data_preparation"]["test_size"]
    max_num_samples_per_class = parameters["data_preparation"][
        "max_num_samples_per_class"
    ]
    random_state = parameters["data_preparation"]["random_state"]

    # Remove rows with null values
    data.dropna(inplace=True)

    # Split data into text (X) and category (y)
    X = np.array(data.narrative)
    y = np.array(data.category)

    # Clean text
    X_clean = text_cleaner(X)

    # Encode the target variable
    y_encoded, tle = label_encoder(y)

    # Split data into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X_clean,
        y_encoded,
        stratify=y_encoded,
        test_size=test_size,
        random_state=random_state,
    )

    # Randomly under sample the training dataset
    X_train_resampled, y_train_resampled = random_under_sampler(
        X_train, y_train, max_num_samples_per_class, random_state=random_state
    )

    # Add logs
    logger = logging.getLogger(__name__)
    logger.info("[manual]: Train dataset size: %.0f", len(X_train_resampled))
    logger.info("[manual]: Test dataset size: %.0f", len(X_test))

    return X_train_resampled, X_test, y_train_resampled, y_test, tle


def train_model(X_train: pd.DataFrame, y_train: pd.Series, parameters: Dict[str, Any]):
    """Train a text classifier."""

    # Unpack parameters
    vectorizer_parameters = parameters["model_training"]["vectorizer_parameters"]
    classifier_parameters = parameters["model_training"]["classifier_parameters"]

    # Create a text classification pipeline: vectorizer + classifier
    pipe_steps = []
    vectorizer = TfidfVectorizer(**vectorizer_parameters)
    pipe_steps.append(("vec", vectorizer))
    classifier = XGBClassifier(**classifier_parameters)
    pipe_steps.append(("clf", classifier))
    text_classifier = Pipeline(pipe_steps)

    # Train a text classifier
    text_classifier.fit(X_train, y_train)

    return text_classifier


def evaluate_model(
    clf: pickle,
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
):
    """Uses a trained model to create predictions."""

    # Compute predictions
    y_train_pred = clf.predict(X_train)
    y_test_pred = clf.predict(X_test)

    # Generate reports
    metrics_report_train = classifier_metrics_report_generator(y_train, y_train_pred)
    metrics_report_test = classifier_metrics_report_generator(y_test, y_test_pred)

    # Add logs
    logger = logging.getLogger(__name__)
    logger.info(
        "[manual]: Train metric report:\n%s", json.dumps(metrics_report_train, indent=4)
    )
    logger.info(
        "[manual]: Test metric report:\n%s", json.dumps(metrics_report_test, indent=4)
    )

    return metrics_report_train, metrics_report_test, y_train_pred, y_test_pred
