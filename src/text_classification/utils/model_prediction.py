"""Module that contains common functions used in model prediction"""

import pickle


class TextClassPredictor():
    """Class to predict text category using trained models.

    Args:
        tle: pickle of the target label encoder.
        clf: pickle of the classifier.
        ndigits: number of digits of the probability.

    Returns:
        y_pred: Prediction of the target variable.
    """
    def __init__(self, tle: pickle, clf: pickle, ndigits: int = 4):
        self.tle = tle
        self.clf = clf
        self.ndigits = ndigits

    def predict(self, x: str):
        """Predict text category.

        Args:
            x: text to classify its category - narrative

        Returns:
            y: Prediction of the target variable - category
        """
        y_encoded = self.clf.predict([x])
        y = self.tle.inverse_transform(y_encoded)[0]
        y_proba = max(self.clf.predict_proba([x])[0])
        response = {'category': y, 'probability': round(y_proba, self.ndigits)}
        return  response
