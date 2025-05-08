from fastapi import FastAPI

app = FastAPI(
    title="Tech Challenge",
    version="0.0.1",
    description="Projeto do Tech Challenge Fiap"
)

@app.get("/")
async def home():
    return "Hello World"