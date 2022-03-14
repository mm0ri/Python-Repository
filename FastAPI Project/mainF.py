from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/items/{item_id}&{item_id2}")
async def read_item(item_id: int, item_id2: int):
    return {"item_id": item_id, "item_id2": item_id2}
