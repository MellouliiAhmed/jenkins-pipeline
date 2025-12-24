from fastapi import FastAPI

app = FastAPI()

@app.get("/api/data")
def get_data():
    print("get_data")
    return {
        "id": 1,
        "name": "Static item",
        "status": "success"
    }
