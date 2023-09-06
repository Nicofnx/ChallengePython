from pydantic import BaseModel

class InputData(BaseModel):
    field_1: str
    author: str
    description: str
    my_numeric_field: int