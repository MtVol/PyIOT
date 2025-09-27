from pydantic import BaseModel

class PatienData(BaseModel):
    N:	int
    P:	int
    K:	int
    temperature: float
    humidity: float
    ph: float
    rainfall: float
    model: int

