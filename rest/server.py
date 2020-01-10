import uvicorn
from fastapi import FastAPI
from pkg.constants.version import SOFTWARE_VERSION

app = FastAPI()


@app.get('/')
async def root():
    return {
        'software': SOFTWARE_VERSION,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
