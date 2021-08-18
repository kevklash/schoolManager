from connection import client as cl, test_connection, print_db_names, database, collection
from repository import insert, retrieve, retrieve_filter, update, delete
import os


if __name__ == '__main__':
    while True:
        os.system("cls")
        print("###Gestión de Centros Escolares - Menu###")
        print("1. Crear un registro")
        print("2. Ver todos los registros")
        print("3. Buscar un Centro Escolar por nombre")
        print("4. Actualizar un registro por ID")
        print("5. Eliminar un registro por ID")
        print("6. Salir")

        option = input("Seleccione la opción: ")

        if option == "1":
            codigo = input("Digite un código numérico para el Centro Escolar: ")
            nombre = input("Digite el nombre del Centro Escolar: ")
            municipio = input("Digite el municipio del Centro Escolar: ")
            departamento = input("Digite el departamento del Centro Escolar: ")
            insert(codigo, nombre, municipio, departamento)
            input("Presione Enter para continuar...")

        elif option == "2":
            retrieve()
            input("Presione Enter para continuar...")

        elif option == "3":
            nombre = input("Digite el nombre del Centro Escolar: ")
            retrieve_filter(nombre)
            input("Presione Enter para continuar...")

        elif option == "4":
            codigo = input("Digite un código del Centro Escolar a actualizar: ")
            nombre = input("Digite el nombre del Centro Escolar: ")
            municipio = input("Digite el municipio del Centro Escolar: ")
            departamento = input("Digite el departamento del Centro Escolar: ")
            update(codigo, nombre, municipio, departamento)
            input("Presione Enter para continuar...")

        elif option == "5":
            codigo = input("Digite un código del Centro Escolar a eliminar: ")
            delete(codigo)
            input("Presione Enter para continuar...")

        elif option == "6":
            print("Terminando sesión. Adiós")
            break

        else:
            print("Seleccione una opción válida")
            input("Presione Enter para continuar...")
            continue
