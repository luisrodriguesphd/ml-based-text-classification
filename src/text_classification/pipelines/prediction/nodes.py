import logging
import pickle
from typing import Any, Dict

from text_classification.utils.data_prep import text_cleaner
from text_classification.utils.model_prediction import TextClassPredictor


def make_prediction(
    tle: pickle,
    clf: pickle,
    parameters: Dict[str, Any],
):
    """Uses a trained model to create predictions.

    Args:
        tle: pickle of the target label encoder.
        clf: pickle of the classifier.
        parameters: dictornary with the narrative to classify.

    Returns:
        prediction: dictonary with predicted category and its probabiltiy.
    """

    # Unpack parameters
    narrative = parameters["model_prediction"]["narrative"]

    # Make prediction
    tcp = TextClassPredictor(
        text_cleaner=text_cleaner, target_encoder=tle, classfier=clf
    )
    prediction = tcp.predict(narrative)

    # Add logs
    logger = logging.getLogger(__name__)
    logger.info("[manual]: Predicted output: %s", prediction)

    return prediction
