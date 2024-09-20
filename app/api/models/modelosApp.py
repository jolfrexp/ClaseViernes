from sqlalchemy import Column,Integer,String,Float,Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
#crear una instancia de la base para crear tablas
Base = declarative_base()
#listado de modelo de la application
#Usuario
class Usuario(Base):
    __tablename__ ='Usuario'
    id = Column(Integer, primary_key=True, autoincrement=True, notnull= False)
    nombre = Column(String(50),nullable= False)
    edad = Column(Integer)
    telefono = Column(String(50),nullable = False)
    correo = Column(String(100),nullable = False)
    contraseña = Column(String(100),nullable = False)
    fechaRegistro = Column(Date,nullable= False)
    ciudad = Column(String(50),nullable = False)

#gasto
class Gasto(Base):
    __tablename__ = 'Gasto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    monto  = Column(String(50),nullable =False)
    fecha = Column(Date,nullable = False)
    descripcion = Column(String(50),nullable=False)
    usuario_id = Column(Integer)
#categoria
class Categoria(Base):
    __tablename__ = 'Categoria'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria = Column(String(50),nullable = False)
    descripcion = Column(String (50), nullable=False)
    fotoicono = Column(String(50),nullable=False)
#metodos de pago
class Metodos(Base):
    __tablename__ = 'Metodo_pago'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo = Column(String(50),nullable = False)
    descripcion = Column(String (50), nullable=False)
#factura
class Factura(Base):
    __tablename__ = 'Factura'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date,nullable = False)
    usuario_id = Column(Integer)
    metodo_id = Column(Integer)
    categoria_id = Column(Integer)
    gasto_id = Column(Integer)
    subtotal  = Column(String(50),nullable =False)
    total  = Column(String(50),nullable =False)