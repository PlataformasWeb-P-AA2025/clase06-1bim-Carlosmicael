from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine

import csv

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objeto de tipo
# Saludo

miSaludo = Saludo2()
miSaludo.mensaje = "Tardes Buenas"
miSaludo.tipo = "Formal"

miSaludo2 = Saludo2()
miSaludo2.mensaje = "Noches Buenas"
miSaludo2.tipo = "Informal"

import csv

# Abrir el archivo CSV
with open('saludos.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo, delimiter='|')  # Usa "|" como delimitador

    for fila in lector:
        saludo = fila['saludo']
        tipo = fila['tipo']
        origen = fila['origen']

        # Aquí puedes acceder a cada campo
        print(f"Saludo: {saludo}, Tipo: {tipo}, Origen: {origen}")
        
        # Si quieres acceder a "Buenos días", por ejemplo:
        if saludo == "Buenos días":
            print("→ Encontrado:", saludo, tipo, origen)



# se agrega el objeto miSaludo
# a la entidad Saludo a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos demobase.db
session.add(miSaludo)
session.add(miSaludo2)

# se confirma las transacciones
session.commit()
