from fastapi import FastAPI
from pydantic import BaseModel
from business_logic import create_groups

app = FastAPI()


class Item(BaseModel):
    n: int
    names: list[str]


@app.put("/creategroups")
async def root(item: Item):
    return {"groups": create_groups(item.names, item.n)}
