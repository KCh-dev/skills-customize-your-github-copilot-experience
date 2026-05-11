from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

items = {
    1: {"name": "Notebook", "description": "A plain notebook", "price": 4.99},
    2: {"name": "Pen", "description": "Blue ink pen", "price": 1.99},
}

@app.get("/items/")
def list_items():
    return [dict(id=item_id, **item_data) for item_id, item_data in items.items()]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return dict(id=item_id, **items[item_id])

@app.post("/items/")
def create_item(item: Item):
    next_id = max(items.keys(), default=0) + 1
    items[next_id] = item.dict()
    return dict(id=next_id, **items[next_id])

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item.dict()
    return dict(id=item_id, **items[item_id])

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"detail": "Item deleted"}
