from fastapi import APIRouter

from schemas.diabetes_schemas import PatienData
from services.diabetes_service import diabetes_prediction


router = APIRouter()

@router.post("/predict")
async def patient_predict(data: PatienData):
    print("patient data ", data.identificacion_number)

    
    Prediction = diabetes_prediction(data)

    return {"prediction": Prediction}
