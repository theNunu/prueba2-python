from typing import Union

from fastapi import FastAPI
from models.items_model import Item
from models.mascotas_models import Mascota
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/mascotas")
def guardar_mascota(mascota: Mascota):
        return {""}