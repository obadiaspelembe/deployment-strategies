
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/app/")
async def root():
    return HTMLResponse(content="Hello there from core root v1", status_code=200)
 