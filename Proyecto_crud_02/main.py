from http.client import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

#Modelo de carros utilizados Pydantic
class Carro(BaseModel):
    id: int
    marca: str
    modelo: int

class Moto(BaseModel):
    id: int
    marca: str
    modelo: int    
#<Datos simulados

carros =[
    Carro(id=1, marca="Toyota", modelo=2020),
    Carro(id=2, marca="Honda", modelo=2019),
    Carro(id=3, marca="Ford", modelo=2018),
    Carro(id=4, marca="Chevrolet", modelo=2017),
    Carro(id=5, marca="Volkswagen", modelo=2016),
    Carro(id=6, marca="BMW", modelo=2015),
    
]

motos =[
    Moto(id=1, marca="Yamaha", modelo=2020),
    Moto(id=2, marca="Honda", modelo=2019),
    Moto(id=3, marca="Harley-Davidson", modelo=2018),
    Moto(id=4, marca="Suzuki", modelo=2017),
    Moto(id=5, marca="Kawasaki", modelo=2016),
    Moto(id=6, marca="Ducati", modelo=2015),
]

# crear la aplicacion FastApi
app = FastAPI()

#Ruta para renderizar el archivo HTML
@app.get("/")
async def home():
    return """

"""

#Obtener la lista de carro GET

@app.get("/carros", response_model=List[Carro])
async def get_carros():
    return carros

#Crear un nuevo carro POST
@app.post("/carros", status_code=201)
async def create_carro(carro: Carro):
    carros.append(carro)
    return {"message": "Carro creado exitosamente"}


#Actualizar un carro PUT
@app.put("/carros/{id}")
async def update_carro(id: str, carro: Carro):
    for index, c in enumerate(carros):
        if c.id == int(id):
            carros[index] = carro
            return {"message": "Carro actualizado exitosamente"} 
    raise HTTPException(status_code=404, detail="Carro no encontrado")

#Eliminar un carro DELETE
@app.delete("/carros/{id}")
async def delete_carro(id: str):
    for index, c in enumerate(carros):
        if c.id == int(id):
            carros.pop(index)
            return {"message": "Carro eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Carro no encontrado")
   
#MOTOS

@app.get("/motos", response_model=List[Moto])
async def get_motos():
    return motos

#Crear un nuevo Moto POST
@app.post("/motos", status_code=201)
async def create_moto(moto: Moto):
    motos.append(moto)
    return {"message": "moto creada exitosamente"}


#Actualizar un Moto PUT
@app.put("/motos/{id}")
async def update_moto(id: str, moto: Moto):
    for index, c in enumerate(motos):
        if c.id == int(id):
            motos[index] = moto
            return {"message": "moto actualizada exitosamente"} 
    raise HTTPException(status_code=404, detail="moto no encontrada")

#Eliminar un Moto DELETE
@app.delete("/motos/{id}")
async def delete_moto(id: str):
    for index, c in enumerate(motos):
        if c.id == int(id):
            motos.pop(index)
            return {"message": "Moto eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Moto no encontrada")