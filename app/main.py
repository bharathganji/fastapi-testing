from fastapi import FastAPI
import os

PORT = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT is not set

# Create an instance of the FastAPI application
app = FastAPI()

# Define a root endpoint that returns a welcome message
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Define an endpoint to get an item by ID
@app.get("/items/{item_id}")
async def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

# Define an endpoint to create a new item
@app.post("/items/")
async def create_item(item: dict):
    return {"message": "Item created successfully", "item": item}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)