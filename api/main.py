from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware # 1. Add this line
import joblib
import pandas as pd
import os

app = FastAPI()

# 2. Add this block right here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # This allows the connection
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("models/fraud_model.pkl")

@app.get("/", response_class=HTMLResponse)
def home():
    base_path = os.getcwd() 
    file_path = os.path.join(base_path, "templates", "index.html")
    with open(file_path, "r") as f:
        return f.read()

@app.post("/predict")
def predict_fraud(amount: float, hour: int):
    input_data = pd.DataFrame([[amount, hour]], columns=['amount', 'hour'])
    prediction = model.predict(input_data)[0]
    status = "🚨 FRAUD DETECTED" if prediction == 1 else "✅ TRANSACTION SAFE"
    return {"result": status}