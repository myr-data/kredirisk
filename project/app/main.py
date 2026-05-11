from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()

model = pickle.load(open(r"D:\Codes\ML Credit Risk\project\models\best_model_xgboost.pkl", "rb"))

class InputData(BaseModel):
    person_age: int
    person_income_log: float
    person_home_ownership: str
    person_emp_length: float
    loan_intent: str
    loan_grade: str
    loan_amnt: int
    loan_int_rate: float
    loan_percent_income: float
    cb_person_default_on_file: int
    cb_person_cred_hist_length: int

@app.post("/predict")
def predict(data: InputData):

    df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(proba)
    }
    
@app.get("/")
def home():
    return {"status": "API running"}