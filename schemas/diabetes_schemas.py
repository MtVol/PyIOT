from pydantic import BaseModel

class PatienData(BaseModel):
    firs_name: str
    last_name: str
    identificacion_number: str
    pregnancies: int
    grucose: int
    bloodpressure: int
    skinthickness: int
    insulin: int
    bmi: float
    diabetespedigreefuncion: float
    age: int
    
