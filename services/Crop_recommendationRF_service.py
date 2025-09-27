import pickle

import numpy as np
from schemas.Crop_recommendationRF_schemas import PatienData

with open('RFCR132.pkl','rb') as file:
    RF_model2 = pickle.load(file)

with open('SVMCR132.pkl','rb') as file:
    SVM_model2 = pickle.load(file)

labels = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans',
 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes',
 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton',
 'jute', 'coffee']

def crop_prediction(data: PatienData):

    xin = np.array([
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]).reshape(1,7)

    if data.model == 1:
        prediction = SVM_model2.predict(xin)
        print("predicction: ",prediction,"SMV")
    else:
        prediction = RF_model2.predict(xin)
        print("predicction: ",prediction,"Random Forest")

    


    return prediction[0]


    