from fastapi import APIRouter, Body

from jonas.bussiness import ModelBussines
from jonas.presentation.schemas import PredictData

jonas = APIRouter(prefix="/api/v1/jonas", tags=["jonas"])


@jonas.post("/train/", status_code=200, description="Train model with current data")
def train():
    return {"model_id": ModelBussines.train()}

@jonas.get("/metric/{model_id}", status_code=200, description="Get model metrics")
def metric(model_id: str):
    return {"recall": ModelBussines.get_metrics(model_id)}

@jonas.post("/predict/{model_id}", description="Predict data on trained model")
def predict(model_id: str, predict_data: PredictData = Body(..., description="predict data")):
    return {"prediction": ModelBussines.predict(model_id, predict_data.model_dump())}