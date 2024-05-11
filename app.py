from fastapi import FastAPI
import requests
import pandas as pd
import numpy as np

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}