from connection import client as cl, collection, database, print_db_names


def insert(codigo, nombre, departamento, municipio):
    dbquery = {"_id": codigo}
    results = collection.find(dbquery).sort("_id")
    if results.count() > 0:
        print("El código proporcionado ya existe, intente nuevamente")
    else:
        document = {"_id": codigo, "nombre": nombre, "municipio": municipio, "departamento": departamento}
        item = collection.insert_one(document)
        print(item)


def retrieve():
    for item in collection.find().sort("_id"):
        print(item)


def retrieve_filter(name):
    dbquery = {"nombre": name}
    results = collection.find(dbquery).sort("_id")
    if results.count() == 0:
        print("No se encontraron resultados, intente de nuevo.")
    else:
        for item in results:
            print(item)


def delete(code):
    dbquery = {"_id": code}
    results = collection.find(dbquery).sort("_id")
    if results.count()== 0:
        print("No se encontró el id proporcionado, intente de nuevo.")
    else:
        item = collection.delete_one(dbquery)
        print(item)


def update(code, nombre, departamento, municipio):
    dbquery = {"_id": code}
    results = collection.find(dbquery).sort("_id")
    if results.count() == 0:
        print("No se encontró el id proporcionado, intente de nuevo.")
    else:
        values = {"$set": {"nombre": nombre, "municipio": municipio, "departamento": departamento}}
        item = collection.update_one(dbquery, values)
        print(item)
