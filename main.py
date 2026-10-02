print("Proyecto colaborativo - Módulo de saludo")

def menu():
    print("1. Saludar")
    print("2. Mostrar integrantes")
    print("3. Realizar operación")

menu()

def saludar():
    nombre = input("Ingresa tu nombre: ")
    print("Hola,", nombre)