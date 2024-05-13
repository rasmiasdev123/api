from fastapi import FastAPI
import requests
import pandas as pd
import numpy as np
from helper import fetch_fno

app = FastAPI()




@app.get("/")
def read_root():
    result = fetch_fno()
    print(result)
    return {"result": "this is for testing"}