from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.models.modelosApp import Usuario
from app.database.configuration import sessionLocal, engine


#Para que un api funciones debe tener un archivo enrutador

rutas = APIRouter() #ENDPOINTS

#Crear una funcion para establer cuando yo quiera y necesite
#conexion a la base de datos
def getDataBase():
    
    basedatos = sessionLocal()
    try:
        yield basedatos
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        basedatos.rollback()
        raise HTTPException(status_code=500, detail="Error al conectar con la base de datos")
    finally:
        basedatos.close()
#PROGRAMACION DE CADA UNO DE LOS SERVICIOS QUE OFRECERA NUESTRA API
#REGISTRANDO O GURADANDO UN USUARIO EN BD
@rutas.post("/Usuarios")
def guardarUsuario(datosPeticion:UsuarioDTOPeticion,db:Session=Depends(getDataBase)):
    try:
        usuario=Usuario(
            nombre=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            ciudad=datosPeticion.ciudad,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as e:
        print(f"Error al guardar el usuario: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al guardar el usuario")
@rutas.get("/Usuarios")
def buscarUsuario():
    pass
@rutas.put("/Usuarios")
def modificarUsuario():
    pass
@rutas.delete("/Usuarios")
def eliminarUsuario():
    pass
            
