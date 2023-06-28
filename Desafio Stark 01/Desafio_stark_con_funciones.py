from data_stark import lista_personajes
from funciones import *
from Desafio_stark import *
import os


while True:
    os.system("cls")
    opcion = menu_00()
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
    elif opcion == 0:
        print("Siguiente menu...")
        input("Precione cualquier boton...")
        os.system("cls")
        break
    else:
        print("Opción inválida. Intente de nuevo.")


if opcion == 0:
    while True:
        os.system("cls")
        opcion = menu_01()
        os.system("cls")

        match opcion:
            case 1:
                imprimir_heroes_masculino(lista_personajes)
                input("Precione cualquier boton...")

            case 2:
                imprimir_heroes_femenino(lista_personajes)
                input("Precione cualquier boton...")

            case 3:
                heroe_mas_alto_m = buscar_heroe_mas_alto_masculino(lista_personajes)
                input("Precione cualquier boton...")
            case 4:
                heroe_mas_alto_f = buscar_heroe_mas_alto_femenino(lista_personajes)
                input("Precione cualquier boton...")

            case 5:
                heroe_mas_bajo_m = buscar_heroe_mas_bajo_masculino(lista_personajes)
                input("Precione cualquier boton...")

            case 6:
                heroe_mas_bajo_f = buscar_heroe_bajo_femenino(lista_personajes)
                input("Precione cualquier boton...")

            case 7:
                altura_promedio_masculino(lista_personajes)
                input("Precione cualquier boton...")

            case 8:
                altura_promedio_femenino(lista_personajes)
                input("Precione cualquier boton...")

            case 9:
                
                informar_nombres(heroe_mas_alto_m, heroe_mas_alto_f, heroe_mas_bajo_m, heroe_mas_bajo_f)
                input("Precione cualquier boton...")

            case 10:
                cantidad_heroes_color_ojos(lista_personajes)
                input("Precione cualquier boton...")

            case 11:
                cantidad_heroes_color_pelo(lista_personajes)
                input("Precione cualquier boton...")

            case 12:
                cantidad_heroes_inteligencia(lista_personajes)
                input("Precione cualquier boton...")

            case 13:
                heroes_color_ojos(lista_personajes)
                input("Precione cualquier boton...")

            case 14:
                heroes_color_pelo(lista_personajes)
                input("Precione cualquier boton...")

            case 15:
                heroes_inteligencia(lista_personajes)
                input("Precione cualquier boton...")

            case 16:
                input("Saliendo...")
                break

            case _:
                print("Error, opcion invalida...")
                break
                
                
        

    






