import uvicorn
import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class toyotacar(BaseModel):
    model: str
    year: int
    transmission: str
    mileage: int
    fuelType: str
    mpg: float
    engineSize: float


app = FastAPI()


@app.get("/")
def read_root():
    return {"Predict": "Used_car_ price"}


@app.post("/predict")
def predict(toyota_car: toyotacar):

    model_pkl_file = "model/model_rf.pkl"
    model_rf = joblib.load(model_pkl_file)

    # Create a pandas dataframe and select the features the current model expects
    input_data = pd.DataFrame([[toyota_car.year, 
                                toyota_car.fuelType, 
                                toyota_car.engineSize,
                                toyota_car.mileage]], 
                              columns=['year', 'fuelType', 'engineSize', 'mileage'])
    
    prediction = model_rf.predict(input_data)

    # Cast the prediction to int
    prediction = int(prediction[0])

    # If the prediction is not valid then we raise an error
    if prediction < 0:
        raise HTTPException(status_code=400, detail="Invalid prediction")

    return {"Toyota used car price suggested": prediction}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")