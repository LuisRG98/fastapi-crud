from fastapi import FastAPI, Path, Query

import models
import service

app = FastAPI()


clase = service.InventoryService()


@app.get("/")
def show_item():
    return clase.show_items()


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="ID of item to info of")):
    return clase.get_item(item_id)


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: models.Item):
    return clase.add_product(item_id, item)


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: models.UpdateItem):
    return clase.update_product(item_id, item)


@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="ID of item to delete")):
    return clase.delete_item(item_id)
