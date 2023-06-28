from data_stark import lista_personajes
from funciones import *
import os


while True:
    # Mostrar menú de opciones
    os.system("cls")
    print("Menú de opciones:")
    print("1. Imprimir nombre de los heroes")
    print("2. Imprimir nombre y altura de los heroes")
    print("3. Buscar superheroe mas alto")
    print("4. Buscar superheroe mas bajo")
    print("5. Promedio de altura de los heroes")
    print("6. Identidad del heroe mas alto o mas bajo")
    print("7. Super heroe mas pesado y menos pesado")
    print("8. Salir")
    opcion = int(input("\nIngrese la opción deseada: "))
    os.system("cls")

    if opcion == 1:
        imprimir_heroes(lista_personajes)
        input("Precione cualquier boton...")
        os.system("cls")
        
    elif opcion == 2:
        imprimir_heroe_altura(lista_personajes)
        input("Precione cualquier boton...")
        os.system("cls")

    elif opcion == 3:
        nombre, altura = heroe_mas_alto(lista_personajes)
        print(f"El heroe mas alto es {nombre} con una altura de {altura} cm")
        input("Precione cualquier boton...")
        os.system("cls")

    elif opcion == 4:
        nombre, altura = heroe_mas_bajo(lista_personajes)
        print(f"El heroe mas bajo es: {nombre} con una altura de: {altura} cm")
        input("Precione cualquier boton...")
        os.system("cls")

    elif opcion == 5:
        promedio = heroe_altura_promedio(lista_personajes)
        print(f"El promedio de la altura de los heroes es: {promedio:.2f} cm")
        input("Precione cualquier boton...")
        os.system("cls")

    elif opcion == 6:
        nombre, altura = heroe_mas_alto(lista_personajes)
        identidad = heroe_buscar_identidad(nombre,lista_personajes)
        print(f"La identidad del heroe mas alto es: {identidad}")

        #identidad del mas bajo
        nombre, altura = heroe_mas_bajo(lista_personajes)
        identidad = heroe_buscar_identidad(nombre, lista_personajes)
        print(f"La identidad del heroe mas bajo es: {identidad}")
        input("Precione cualquier boton...")
        os.system("cls")
        
    elif opcion == 7:
        nombre_mas_pesado,peso_mas_alto, nombre_menos_pesado, peso_menos_pesado = heroe_mas_y_menos_pesado(lista_personajes)
        print(f"El heroe mas pesado es: {nombre_mas_pesado} con: {peso_mas_alto} kg")
        print(f"El heroe mas liviano es: {nombre_menos_pesado} con: {peso_menos_pesado} kg")
        input("Precione cualquier boton...")
        os.system("cls")

    elif opcion == 8:
        print("Saliendo del programa...")
        input("Precione cualquier boton...")
        os.system("cls")
        break
    else:
        print("Opción inválida. Intente de nuevo.")









