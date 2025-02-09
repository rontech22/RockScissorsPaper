import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/classic_options_es")
def get_classic_opts_es():
    options = ("piedra", "papel", "tijera")
    return options

@app.get("/classic_options_en")
def get_classic_opts_en():
    options = ("rock", "scissors", "paper")
    return options

@app.get("/rpsls_options_en")
def get_rpsls_opts_en():
    options = ("rock", "scissors", "paper","lizard","spock")
    return options