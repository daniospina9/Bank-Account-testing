from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_usd_currency():
    return [{"USD": 4500}]