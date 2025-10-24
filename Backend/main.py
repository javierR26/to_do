from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Lista to do"])
async def traer():
    return "mira todos"

@app.get("/{id}", tags=["Lista to do"])
async def traerById(id):
    return f"mira todos {id}"

@app.post("/", tags=["Lista to do"])
async def crear():
    return "se creo"

@app.put("/{id}", tags=["Lista to do"])
async def actulizar(id):
    return f"se actulizo todo {id}"

@app.patch("/{id}", tags=["Lista to do"])
async def actulizarAlgo(id):
    return f"se actulizo una parte{id}" 

@app.delete("/{id}", tags=["Lista to do"])
async def eliminar(id):
    return f"se elimino {id}"       