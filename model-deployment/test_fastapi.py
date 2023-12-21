from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# App Instance
app = FastAPI()

# Create a function
# Decorate with `get` operator with a `route` / for the landing page
@app.get("/")
async def read_root():
    return {
        "Hello" : "World"
    }
    
# Second Function
# Using Optional typing
# Using type hint, one required one optional
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id" : item_id,
        "q" : q
    }