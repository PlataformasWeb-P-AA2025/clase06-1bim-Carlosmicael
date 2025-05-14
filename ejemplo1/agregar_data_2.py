from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine

import csv

Session = sessionmaker(bind=engine)
session = Session()

import csv

with open('data/saludos_mundo.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo, delimiter='|') 
    for fila in lector:
        session.add(Saludo2(mensaje=fila['saludo'],tipo=fila['tipo'],origen=fila['origen']))



# se agrega el objeto miSaludo
# a la entidad Saludo a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos demobase.db
# se confirma las transacciones
session.commit()
