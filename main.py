from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(
    title="DevOps Gün1 - FastAPI",
    description="Linux/Docker pratik app",
    version="1.0.0"
)

class PredictRequest(BaseModel):
    feature1: float
    feature2: Optional[float] = 0.0

@app.get("/")
def root():
    return {"message": "DevOps Roadmap Gün1 hazır!", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "OK", "timestamp": "2026-01-22"}

@app.post("/predict")
def predict(data: PredictRequest):
    # Senin ML thesis'inden ilham: basit linear model
    prediction = data.feature1 * 2.5 + data.feature2 * 1.3 + 0.5
    return {
        "input": data.dict(),
        "prediction": round(prediction, 2),
        "model": "linear_devops_v1"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        log_level="info"
    )
