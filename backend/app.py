from fastapi import FastAPI, Query
from detection import assess_hostname

app = FastAPI()

@app.get("/check")
def 
