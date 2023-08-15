import uvicorn
from fastapi import FastAPI

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api",
)

@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
