from fastapi import FastAPI
import requests
import pandas as pd
import numpy as np
from helper import fetch_fno

app = FastAPI()




@app.get("/")
def read_root():
    stocks_list = fetch_fno()
    return {"fno_list": stocks_list}