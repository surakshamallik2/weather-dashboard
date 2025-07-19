from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/weather/{city}")
def get_weather(city: str):
    return {"city": city, "temperature": "28°C", "condition": "Sunny"}
