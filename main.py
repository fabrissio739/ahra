from fastapi import FastAPI

app = FastAPI()

@app.get("/Ola-fabrissio")
def read_root():
    return {"message": "esse e o api do fabrissio!"}

@app.get("/multiplicacao")
def read_root(v1: int, v2: int):
    res = v1 * v2
    return {"resultado": res}

@app.put("/cadastra-atendimento")
def cadastra_atendimento(Body: dict = (...)):
    return {"menssage": Body}