from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str
#     price: float
#     tax: float = None

# class User(BaseModel):
#     username: str
#     full_name: str = None


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/items")
# async def create_item(item: Item):
#     return {"item": item}

# @app.post("/users")
# async def create_user(user: User):
#     return {"user": user}