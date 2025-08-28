from pydantic import BaseModel
from typing import Union

class Mascota (BaseModel):
    tipo_animal : str
    nombre: str
    edad: int