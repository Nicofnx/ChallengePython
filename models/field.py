from pydantic import BaseModel

# Creo la clase de los campos
class InputData(BaseModel):
    field_1: str
    author: str
    description: str
    my_numeric_field: int