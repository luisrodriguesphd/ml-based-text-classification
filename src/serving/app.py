"""RESTful API in Python to serve predictions from the trained model."""

import uvicorn
from fastapi import FastAPI
from kedro.io import MemoryDataSet

from serving.settings import catalog, parameters, predict_pipeline, runner
from serving.utils import (
    predict_request,
    predict_respose,
    update_parameters_with_predict_request,
)

app = FastAPI(title=parameters["model_serving"]["title"])


@app.get("/")
def read_root():
    return {"message": "ok"}


@app.post("/predict")
def predict(request: predict_request) -> predict_respose:
    """Predict the category for a given narrative."""
    predict_parameters = update_parameters_with_predict_request(parameters, request)
    catalog.add("parameters", MemoryDataSet(predict_parameters), replace=True)
    pipeline_output = runner.run(pipeline=predict_pipeline, catalog=catalog)
    print(pipeline_output)
    print(type(pipeline_output))
    print(pipeline_output["prediction"])
    response = predict_respose(
        category=pipeline_output["prediction"]["y_pred"],
        probability="%.4f" % pipeline_output["prediction"]["y_proba"],
    )
    return response


if __name__ == "__main__":
    HOST = parameters["model_serving"]["host"]
    PORT = parameters["model_serving"]["port"]
    uvicorn.run("__main__:app", host=HOST, port=PORT, reload=True)
