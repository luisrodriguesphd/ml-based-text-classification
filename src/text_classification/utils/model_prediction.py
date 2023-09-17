"""Module that contains common functions used in model prediction"""

import pickle


class TextClassPredictor:
    """Class to predict text category using trained models.

    Args:
        tle: pickle of the target label encoder.
        clf: pickle of the classifier.
    """

    def __init__(self, tle: pickle, clf: pickle):
        self.tle = tle
        self.clf = clf

    def predict(self, x: str):
        """Predict text category.

        Args:
            x: text to classify its category - narrative

        Returns:
            response: dictonary with predicted category and its probabiltiy.
        """
        y_encoded = self.clf.predict([x])
        y_pred = self.tle.inverse_transform(y_encoded)[0]
        y_proba = max(self.clf.predict_proba([x])[0])
        response = {"y_pred": y_pred, "y_proba": y_proba}
        return response
