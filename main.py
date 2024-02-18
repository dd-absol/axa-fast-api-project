from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from business_logic import create_groups

app = FastAPI()


class Item(BaseModel):
    n: int
    names: list[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "n": 2,
                    "name": [
                        "Alice",
                        "Bob",
                        "Charlotte",
                        "Dylan"
                    ]
                }
            ]
        }
    }


@app.put("/creategroups")
async def creategroups(item: Item):

    if item.n <= 0:
        raise HTTPException(
            status_code=400,
            detail="number of groups cannot be negative or null",
        )

    groups = create_groups(item.names, item.n)

    if groups is None:
        raise HTTPException(
            status_code=400, detail="There are less names than groups"
        )

    return {"groups": groups}
