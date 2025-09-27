import pickle

import numpy as np
from schemas.diabetes_schemas import PatienData

with open('RFDiabetesv132.pkl','rb') as file:
    RF_model2 = pickle.load(file)

labels = ["sano", "Emfermo"]

def diabetes_prediction(data: PatienData):

    xin = np.array([

        data.pregnancies,
        data.grucose,
        data.bloodpressure,
        data.skinthickness,
        data.insulin,
        data.bmi,
        data.diabetespedigreefuncion,
        data.age
    ]).reshape(1,8)
    
    prediction = RF_model2.predict(xin)
    print("predicction: ",prediction)

    return labels[prediction[0]]


    