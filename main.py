from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

class RealEstateFeatures(BaseModel):
    house_age: float
    distance_to_mrt: float
    number_of_convenience_stores: int
    latitude: float

model = joblib.load("reg.pkl")



@app.get("/")
def read_root():
    return {'message': "Estate Price Prediction API"}

@app.post("/predict/")
def predict_price(features: RealEstateFeatures):
    
    data = np.array([[features.house_age, features.distance_to_mrt, 
                      features.number_of_convenience_stores, features.latitude]])

    
    prediction = model.predict(data)

    
    return {"predicted_price": prediction[0]}

