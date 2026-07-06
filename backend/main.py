from fastapi import FastAPI

app = FastAPI(title="AI Debt Relief API")

@app.get("/")
def home():
    return {
        "message": "AI Powered Debt Relief & Financial Recovery Platform API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
