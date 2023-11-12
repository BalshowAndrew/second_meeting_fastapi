from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/hotels")
def get_hotels():
    return "Отель Бридж Резорт 5 звезд"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
