from pydantic import BaseModel, Field


class predict_request(BaseModel):
    id: str = Field(
        None, description="Identification number of the text", example="0141"
    )
    narrative: str = Field(
        None,
        description="Text to classify its category",
        example="current loan provident funding applied refinance provident funding variable interest rate went loan applied refinance downpayment reduce depth also monthly payment locked interest rate day current payment going approximately provided income debt information provident funding provident funding play game interest rate arm went provided every information suspended loan application able reach mortgage broker always get voicemail responded email underwriter approving due ratio",
    )


class predict_respose(BaseModel):
    category: str = Field(None, description="predicted category", example="credit_card")
    probability: float = Field(
        None, description="class probability membership", example=0.9512
    )


def update_parameters_with_predict_request(parameters, request):
    for key in request.__dict__.keys():
        parameters["model_prediction"][key] = getattr(request, key)

    return parameters
