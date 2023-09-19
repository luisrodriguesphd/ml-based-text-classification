"""Module that contains common functions used in model prediction"""

import pickle
from typing import Callable


class TextClassPredictor:
    """Class to predict text category using trained models.

    Args:
        text_cleaner: function to clean the text.
        target_encoder: pickle of the target label encoder.
        classfier: pickle of the classifier.
    """

    def __init__(
        self, text_cleaner: Callable, target_encoder: pickle, classfier: pickle
    ):
        self.text_cleaner = text_cleaner
        self.target_encoder = target_encoder
        self.classfier = classfier

    def predict(self, x: str):
        """Predict text category.

        Args:
            x: text to classify its category - narrative

        Returns:
            response: dictonary with predicted category and its probabiltiy.
        """
        x_clean = self.text_cleaner([x])
        y_encoded = self.classfier.predict(x_clean)
        y_pred = self.target_encoder.inverse_transform(y_encoded)[0]
        y_proba = max(self.classfier.predict_proba([x])[0])
        response = {"y_pred": y_pred, "y_proba": y_proba}
        return response
