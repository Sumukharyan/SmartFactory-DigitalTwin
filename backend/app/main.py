from fastapi import FastAPI

app = FastAPI(
    title="Smart Factory Digital Twin API",
    description="Backend API for Smart Factory Digital Twin Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Smart Factory Digital Twin API"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }