"""
This is a boilerplate pipeline
generated using Kedro 0.18.12
"""

from kedro.pipeline import Pipeline, node, pipeline

from text_classification.pipelines.training.nodes import (
    evaluate_model,
    prepare_data,
    train_model,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=prepare_data,
                inputs=["training_dataset", "parameters"],
                outputs=["X_train", "X_test", "y_train", "y_test", "target_encoder"],
                name="prepare_data",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train", "parameters"],
                outputs="classifier",
                name="train_model",
            ),
            node(
                func=evaluate_model,
                inputs=["classifier", "X_train", "X_test", "y_train", "y_test"],
                outputs=[
                    "metrics_report_train",
                    "metrics_report_test",
                    "y_train_pred",
                    "y_test_pred",
                ],
                name="evaluate_model",
            ),
            # node(
            #    func=validate_model,
            #    inputs=["y_pred", "y_test"],
            #    outputs=["target_encoder", "classifier", "model_type"],
            #    name="validate_model",
            # ),
        ]
    )
