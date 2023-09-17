"""
This is a boilerplate pipeline
generated using Kedro 0.18.12
"""

from kedro.pipeline import Pipeline, node, pipeline

from text_classification.pipelines.prediction.nodes import make_prediction


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=make_prediction,
                inputs=["target_encoder", "classifier", "parameters"],
                outputs="prediction",
                name="make_prediction",
            ),
        ]
    )
