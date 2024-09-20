from pydantic import BaseModel, Field

from datetime import date

class UsuarioDTOPeticion(BaseModel):
    nombre: str
    edad: int
    telefono: str
    correo: str
    contraseña: str
    fechaRegistro: date
    ciudad:str
    class Config:
        orm-mode=True
class UsuarioDTORespuesta(BaseModel):
    id: str
    nombre: str
    telefono: str
    ciudad: str
    class Config:
        orm-mode=True

class GastoDTORespuesta(BaseModel):
    monto = float 
    fecha = date
    descripcion = str
    usuario_id = int
    class Config:
        orm-mode=True
class GastoDTOPeticion(BaseModel):
    monto = float 
    fecha = date
    descripcion = str
    class Config:
        orm-mode=True
class CategoriaDTOPeticion(BaseModel):
    nombreCategoria = str
    descripcion = str
    fotoicono = str
    class Config:
        orm-mode=True
class CategoriaDTORespuesta(BaseModel):
    nombreCategoria = str
    descripcion = str
    fotoicono = str
    class Config:
        orm-mode=True
    
class MetodoPagoDTOPeticion(BaseModel):
    nombreMetodo = str
    descripcion = str
    class Config:
        orm-mode=True
#factura
class MetodoPagoDTORespuesta(BaseModel):
    nombreMetodo = str
    descripcion = str
    class Config:
        orm-mode=True
class FacturaDTORespuesta(BaseModel):
    idFactura = str
    fecha = date
    usuario = str
    metodo = str
    gasto = str
    subtotal = float
    total = float
    class Config:
        orm-mode=True
class FacturaDTOPeticion(BaseModel):
    fecha = date
    usuario_id = int
    metodo_id = int
    categoria_id = int
    gasto_id = int
    subtotal  =  float
    total  = float
    class Config:
        orm-mode=True