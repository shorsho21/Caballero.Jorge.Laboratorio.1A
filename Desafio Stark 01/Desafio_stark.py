from data_stark import lista_personajes
from funciones import *


#Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
def imprimir_heroes_masculino(lista_personajes:list)->None:
    """Recorre la lista imprimiendo por consola el nombre de cada superhéroe de género M

    Args:
        lista_personajes (list): lista de heroes
    """
    for i in range(len(lista_personajes)):
        if "M" == lista_personajes[i]["genero"]:
            print(lista_personajes[i]["nombre"])

# Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F

def imprimir_heroes_femenino(lista_personajes:list)->None:
    """Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F

    Args:
        lista_personajes (list): lista de heroes
    """
    for i in range(len(lista_personajes)):
        if "F" == lista_personajes[i]["genero"]:
            print(lista_personajes[i]["nombre"])

#Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
def buscar_heroe_mas_alto_masculino(lista_personajes:list)->dict:
    """Recorrer la lista y determinar cuál es el superhéroe más alto de género M 

    Args:
        lista_personajes (list): lista de personajes

    Returns:
        dict: retorna el diccionario del heroe M mas alto
    """
    heroe_mas_alto_nombre = None
    heroe_mas_alto_altura = 0.0
    for i in range(len(lista_personajes)):
        if "M" == lista_personajes[i]["genero"]:
            if heroe_mas_alto_altura < float(lista_personajes[i]["altura"]):
                heroe_mas_alto_nombre = lista_personajes[i]["nombre"]
                heroe_mas_alto_m = lista_personajes[i]
                heroe_mas_alto_altura = float(lista_personajes[i]["altura"])
    print(f"El heroe mas alto masculino es {heroe_mas_alto_nombre} con {heroe_mas_alto_altura} cm")

    return heroe_mas_alto_m

#Recorrer la lista y determinar cuál es el superhéroe más alto de género F 

def buscar_heroe_mas_alto_femenino(lista_personajes:list)->dict:
    """Recorrer la lista y determinar cuál es el superhéroe más alto de género F 

    Args:
        lista_personajes (list): lista de heroes

    Returns:
        dict: diccionario del heroe
    """
    heroe_mas_alto_nombre = None
    heroe_mas_alto_altura = 0.0
    for i in range(len(lista_personajes)):
        if "F" == lista_personajes[i]["genero"]:
            if heroe_mas_alto_altura < float(lista_personajes[i]["altura"]):
                heroe_mas_alto_nombre = lista_personajes[i]["nombre"]
                hereo_mas_alto_f = lista_personajes[i]
                heroe_mas_alto_altura = float(lista_personajes[i]["altura"])
    print(f"El heroe mas alto femenino es {heroe_mas_alto_nombre} con {heroe_mas_alto_altura} cm")

    return hereo_mas_alto_f

# Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
def buscar_heroe_mas_bajo_masculino(lista_personajes:list)->dict:
    """Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 

    Args:
        lista_personajes (list): lista de heroes

    Returns:
        dict: diccionario del heroe
    """
    heroe_mas_bajo_nombre = None
    heroe_mas_bajo_altura = 0.0
    bandera_altura = True
    for i in range(len(lista_personajes)):
        if "M" == lista_personajes[i]["genero"]:
            if bandera_altura == True or heroe_mas_bajo_altura > float(lista_personajes[i]["altura"]):
                heroe_mas_bajo_nombre = lista_personajes[i]["nombre"]
                heroe_mas_bajo_m = lista_personajes[i]
                heroe_mas_bajo_altura = float(lista_personajes[i]["altura"])
                bandera_altura = False
    print(f"El heroe mas mas bajo masculino es {heroe_mas_bajo_nombre} con {heroe_mas_bajo_altura} cm")

    return heroe_mas_bajo_m


#Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
def buscar_heroe_bajo_femenino(lista_personajes:list)->dict:
    """Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 

    Args:
        lista_personajes (list): lista de heroes

    Returns:
        dict: diccionario de heroe
    """
    heroe_mas_bajo_nombre = None
    heroe_mas_bajo_altura = 0.0
    bandera_altura = True
    for i in range(len(lista_personajes)):
        if "F" == lista_personajes[i]["genero"]:
            if bandera_altura == True or heroe_mas_bajo_altura > float(lista_personajes[i]["altura"]):
                heroe_mas_bajo_nombre = lista_personajes[i]["nombre"]
                heroe_mas_bajo_f = lista_personajes[i]
                heroe_mas_bajo_altura = float(lista_personajes[i]["altura"])
                bandera_altura = False
    print(f"El heroe mas mas bajo masculino es {heroe_mas_bajo_nombre} con {heroe_mas_bajo_altura} cm")

    return heroe_mas_bajo_f

#Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
def altura_promedio_masculino(lista_personajes:list)->None:
    """#Recorrer la lista y determinar la altura promedio de los  superhéroes de género M

    Args:
        lista_personajes (list): lista de personajes
    """
    sumador = 0
    contador = 0
    promedio = 0
    for i in range(len(lista_personajes)):
        if "M" == lista_personajes[i]["genero"]:
            contador += 1
            sumador += float(lista_personajes[i]["altura"])
    promedio = sumador / contador
    print(f"La altura promedio de los heroes masculinos es: {promedio:.2f} cm")

#Recorrer la lista y determinar la altura promedio de los  superhéroes de género F

def altura_promedio_femenino(lista_personajes:list)->None:
    """Recorrer la lista y determinar la altura promedio de los  superhéroes de género F

    Args:
        lista_personajes (list): lista de heroes
    """
    sumador = 0
    contador = 0
    promedio = 0
    for i in range(len(lista_personajes)):
        if "F" == lista_personajes[i]["genero"]:
            contador += 1
            sumador += float(lista_personajes[i]["altura"])
    promedio = sumador / contador
    print(f"La altura promedio de los heroes femeninos es: {promedio:.2f} cm")

#Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)

#Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def cantidad_heroes_color_ojos(lista_personajes:list)->None:
    """Determinar cuántos superhéroes tienen cada tipo de color de ojos.

    Args:
        lista_personajes (list): lista de heroes
    """
    contador_de_colores = {}
    for i in range (len(lista_personajes)):
        color_ojos = lista_personajes [i]["color_ojos"]
        if color_ojos in contador_de_colores:
            contador_de_colores[color_ojos] += 1
        else:
            contador_de_colores[color_ojos] = 1
    print(contador_de_colores)

#Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def cantidad_heroes_color_pelo(lista_personajes:list)->None:
    """Determina cuántos superhéroes tienen cada tipo de color de pelo.

    Args:
        lista_personajes (list): lista de heroe
    """
    contador_de_colores = {}
    for i in range (len(lista_personajes)):
        color_pelo = lista_personajes[i]["color_pelo"]
        if color_pelo in contador_de_colores:
            contador_de_colores[color_pelo] += 1
        else:
            contador_de_colores[color_pelo] = 1
    print(contador_de_colores)

#Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
def cantidad_heroes_inteligencia(lista_personajes:list)->None:
    """Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 

    Args:
        lista_personajes (list): lista de heroes
    """
    contador_de_inteligencia = {}
    for i in range (len(lista_personajes)):
        tipo_inteligencia = lista_personajes[i]["inteligencia"]

        if tipo_inteligencia == "":
            if "no tiene" in contador_de_inteligencia:
                contador_de_inteligencia["no tiene"] += 1
            else:
                contador_de_inteligencia["no tiene"] = 1

        elif tipo_inteligencia in contador_de_inteligencia:
            contador_de_inteligencia[tipo_inteligencia] += 1
        else:
            contador_de_inteligencia[tipo_inteligencia] = 1
        
        
    print(contador_de_inteligencia)

#Listar todos los superhéroes agrupados por color de ojos.

# def filtrar_lista(lista: list, key: str, valor: str) -> list:
#     lista_filtrada = []
#     for value in lista:
#         if value[key] == valor:
#             lista_filtrada.append(value)
#color sin repetir
def heroes_color_ojos(lista_personajes:list)->None:
    """Listar todos los superhéroes agrupados por color de ojos.

    Args:
        lista_personajes (list): lista de heroes
    """
    lista_sin_repetir = []
    for value in lista_personajes:
        color_ojos = value["color_ojos"]
        if not color_ojos in lista_sin_repetir:
            lista_sin_repetir.append(color_ojos)
    print(lista_sin_repetir)

    for value in range(len(lista_sin_repetir)):
        print("__________________")
        print(lista_sin_repetir[value])
        print("___________________")
        for valor in lista_personajes:
            if valor["color_ojos"] == lista_sin_repetir[value]:
                print(valor["nombre"])




# contador_de_colores = {}
# for heroe in lista_personajes:
#     color_ojos = heroe["color_ojos"]
#     if color_ojos in contador_de_colores:
#         contador_de_colores[color_ojos].append(heroe["nombre"])
#     else:
#         contador_de_colores[color_ojos] = heroe["nombre"]

# print(contador_de_colores)

#Listar todos los superhéroes agrupados por color de pelo.
def heroes_color_pelo(lista_personajes:list)->None:
    """Listar todos los superhéroes agrupados por color de pelo.

    Args:
        lista_personajes (list): _description_
    """
    lista_sin_repetir = []
    for value in lista_personajes:
        color_pelo = value["color_pelo"]
        if not color_pelo in lista_sin_repetir:
            lista_sin_repetir.append(color_pelo)
    print(lista_sin_repetir)


    for value in range(len(lista_sin_repetir)):
        print("__________________")
        print(f"Los heroes con el color de pelo {lista_sin_repetir[value]} son:")
        print("___________________")
        for valor in lista_personajes:
            if valor["color_pelo"] == lista_sin_repetir[value]:
                print(valor["nombre"])


#Listar todos los superhéroes agrupados por tipo de inteligencia
def heroes_inteligencia(lista_personajes:list)->None:
    """Listar todos los superhéroes agrupados por tipo de inteligencia

    Args:
        lista_personajes (list): _description_
    """
    lista_sin_repetir = []
    for value in lista_personajes:
        tipo_inteligencia = value["inteligencia"]

        if tipo_inteligencia == "":
            if not "no tiene" in lista_sin_repetir:
                lista_sin_repetir.append("no tiene")
            

        elif not tipo_inteligencia in lista_sin_repetir:
            lista_sin_repetir.append(tipo_inteligencia)
    
    print(lista_sin_repetir)

    


    for value in lista_sin_repetir:
        print("__________________")
        print(f"Los heroes con la inteligencia {value} son:")
        print("___________________")
        for valor in lista_personajes:
            if valor["inteligencia"] == value:
                print(valor["nombre"])

            if value == "no tiene" and valor["inteligencia"] == "":
                print(valor["nombre"])



#menu 01

def menu_01():
    print("1.Imprimir superheroes de genero masculino")
    print("2.Imprimir superheroes de genero femenino")
    print("3.SupeHeroe mas alto masculino")
    print("4.SuperHeroe mas alto femenino")
    print("5.SuperHeroe mas bajo masculino")
    print("6.SuperHeroe mas bajo femenino")
    print("7.Altura promedio de SuperHeroes masculinos")
    print("8.Altura promedio de SuperHeroes femeninos")
    print("9.Nombre de los SuperHeroes asociado a cada uno de los indicadores anteriores")
    print("10.Cantidad SuperHeroes tienen cada tipo de color de ojos")
    print("11.Cnatidad SuperHeroes tienen cada tipo de color de pelo")
    print("12.Determinar cuantos SuperHeroes tienen cada tipo de inteligencia")
    print("13.Listar todos los SuperHeroes agrupados por color de ojos")
    print("14.Listar todos los SuperHeroes agrupados por color de pelo")
    print("15.Listar todos los SuperHeroes agrupados por tipo de inteligencia")
    print("16.Salir")
    opcion = int(input("\nIngrese la opción deseada: "))

    return opcion



# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)

def informar_nombres(heroe_mas_alto_m, heroe_mas_alto_f, heroe_mas_bajo_m, heroe_mas_bajo_f):
    
    print(f'Identidad Heroe mas alto masculino:{heroe_mas_alto_m["identidad"]}')
    print(f'Identidad Heroe mas alto femenino:{heroe_mas_alto_f["identidad"]}')
    print(f'Identidad Heroe mas bajo masculino:{heroe_mas_bajo_m["identidad"]}')
    print(f'Identidad Heroe mas bajo femenino:{heroe_mas_bajo_f["identidad"]}')