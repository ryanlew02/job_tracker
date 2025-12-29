from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI() #uvicorn main:app --reload --reload-exclude ".venv/*"

items = []

class Item(BaseModel):
    name: str
    is_done: bool = False



@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/items", response_model=list[Item])
async def list_items(limit: int = 10):
    return items[0:limit]



@app.post("/items")
async def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    item = items[item_id]
    return item



