from typing import Optional
from unicodedata import name
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {}

@app.get("/")
def show_item():
    for item in inventory:
        return inventory[item]

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="ID of item to info of")):
    return inventory[item_id]

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error":"Item ID already exists."}
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return{"Error":"Item ID does not exists"}
    
    if item.name != None:
        inventory[item_id].name =  item.name

    if item.price != None:
        inventory[item_id].price =  item.price

    if item.brand != None:
        inventory[item_id].brand =  item.brand

    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="ID of the item to be deleted")):
    if item_id not in inventory:
        return {"Error":"Item does not exists"}
    
    del inventory[item_id]
    return {"Success":"Item deleted"}