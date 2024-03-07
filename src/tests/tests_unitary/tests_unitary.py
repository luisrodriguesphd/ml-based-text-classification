"""Module for unit testing"""

import pytest

from ml_based_text_classification.pipelines.training.nodes import train_model

from .unitary_test_data import data_test_train_model


@pytest.mark.parametrize(argnames="test_data", argvalues=data_test_train_model)
def test_train_model(test_data):
    """unit test for train_model function"""
    params = {
        "model_training": {"vectorizer_parameters": {}, "classifier_parameters": {}}
    }
    vec, clf = train_model(test_data["X"], test_data["y"], params)

    assert vec.__class__.__name__ == test_data["vec_name"]
    assert clf.__class__.__name__ == test_data["clf_name"]
