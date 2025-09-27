from fastapi import APIRouter

from schemas.Crop_recommendationRF_schemas import PatienData
from services.Crop_recommendationRF_service import crop_prediction



router = APIRouter()

@router.post("/predict")
async def patient_predict(data: PatienData):
    
    Prediction = crop_prediction(data)

    return {"prediction": Prediction}
