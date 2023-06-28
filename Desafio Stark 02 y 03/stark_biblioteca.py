import os


def is_float(value):
    """Recibe un string, devuelve True si se puede volver flotante y false si no se puede

    Args:
        value (string): cadena a comprobar

    Returns:
        bool: True o False
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def stark_normalizar_datos(lista:list):
    """Normaliza los datos(Si son strings con numeros los vuelve int or float segun corresponda)

    Args:
        lista (list): recibe la lista de heroes stark
    """
    lista_normalizada = []
    datos_normalizados = False
    if len(lista) == 0:
        print("Error la lista esta vacia")
        return
    for heroe in lista:
        for key, value in heroe.items():
            if isinstance(value, str) and value.isdigit():
                heroe[key] = int(heroe[key])
                datos_normalizados = True
                
                
            elif isinstance(value, str) and is_float(value):
                heroe[key] = float(heroe[key])
                datos_normalizados = True
        lista_normalizada.append(heroe)
                
    if datos_normalizados == True:
        print("Los datos han sido normalizados")
        return lista_normalizada


def obtener_nombre(dict):
    """Recibe un diccionario de un heroe y devuelve: "Nombre: *Nombre del heroe*

    Args:
        dict (dict): diccionario de datos del heroe

    Returns:
        string: devuelve el nombre del heroe
    """
    nombre = f"Nombre: {dict['nombre']}"
    return nombre


def imprimir_dato(string:str):
    """recibe e imprime un string 

    Args:
        string (string): dato a imprimir
    """
    print(string)


def stark_imprimir_nombres_heroes(list:list)->int:
    """Recibe una lista, imprime los nombres de los heroes

    Args:
        list (list): lista de heroes

    Returns:
        int: retorna -1 si la lista esta vacia, de caso contrario no retorna nada solo imprime
    """
    if len(list) == 0:
        print("Error la lista esta vacia")
        return -1

    for nombres in list:
        imprimir_dato(obtener_nombre(nombres))


def obtener_nombre_y_dato(dict:dict, key:str)->str:
    """Recibe el diccionario de un heroe y una key que es el dato a obtener y retorna un string con el nombre y el dato al lado

    Args:
        dict (dict): diccionario del heroe
        key (string): dato a buscar

    Returns:
        str: retorna el nombre y el dato
    """
    dato = f"Nombre: {dict['nombre'] }   | {key}: {dict[key]}"
    return dato


def stark_imprimir_nombres_alturas(list:list)->int:
    """Recibe la lista de heroes, itera e imprime sus nombres

    Args:
        list (list): lista de heroes

    Returns:
        int: retorna -1 si no se cumple las condiciones
    """
    if len(list) == 0:
        return -1
    for heroes in list:
        print(obtener_nombre_y_dato(heroes,"altura"))



def calcular_max(list:list,key:str)->dict:
    """Recibe la lista y la key, itera todos los heroes y retorna el heroe que tiene el valor mas alto en esa key

    Args:
        list (list): lista de heroe
        key (str): key en la que buscar cual tiene el valor mas alto

    Returns:
        dict: retorna el heroe con el valor mas alto
    """
    # if type(list[key]) == str:
    #     print("No se puede calcular el tipo ese tipo de dato")
    #     return
    max = 0
    for value in list:
        if value[key] > max:
            max = value[key]
            heroe = value
    return heroe


def calcular_min(list:list,key:str)->dict:
    """Recibe una lista de heroes, la key, itera los heroes y retorna el heroe con el valor mas bajo de esa key

    Args:
        list (list): lista de heroe
        key (str): la key del heroe en la que buscar el mas bajo

    Returns:
        dict: retorna el heroe con el valor mas bajo
    """
    min = 0
    flag_min = True

    for value in list:
        if flag_min == True or value[key] < min:
            flag_min = False
            min = value[key]
            heroe = value
    return heroe


def calcular_max_min_dato(list:list,maxmin:str,key:str)->dict:
    """Recibe la lista de heroes, el tipo de calculo, la key, retorna el diccionario del heroe que cumple con la condicion

    Args:
        list (list): lista de heroe
        maxmin (str): maximo minimo
        key (str): key del heroe

    Returns:
        dict: retorna el diccionario del heroe que cumple la condicion
    """

    if maxmin == "maximo":
        max =calcular_max(list,key)
        return max

    elif maxmin == "minimo":
        min = calcular_min(list,key)
        return min
    else:
        print("Tipo de dato invalido")
        return -1


def stark_calcular_imprimir_heroe(list:list,maxmin:str,key:str)->int:
    """Recibe la lista de heroes, el tipo de calculo, la key del heroe, imprime el nombre  del heroe, con el valor que le corresponda.

    Args:
        list (list): lista de heroe
        maxmin (str): maximo minimo
        key (str): key del heroe

    Returns:
        int: -1 si es la lista esta vacia
    """
    if len(list) == 0:
        return -1
    
    Heroe_maxmin = calcular_max_min_dato(list,maxmin,key)
    dato = obtener_nombre_y_dato(Heroe_maxmin,key)
    if maxmin == "maximo":
        imprimir_dato(f"Mayor {key}: {dato}")

    if maxmin == "minimo":
        imprimir_dato(f"Menor {key}: {dato}")

    
    
def sumar_dato_heroe(list:list,key:str)->int:
    """Recibe como parametro la lista de heroes y una key, suma los valores de esa key de todos los heroes de la lista

    Args:
        list (list): lista de heroes
        key (str): key del heroe

    Returns:
        int: los valores de la key de todos los heroes sumados.
    """
    sumador = 0
    for value in range(len(list)):
        if type(list[value]) == dict and len(list[value]) != 0 :
            sumador += list[value][key]
        else:
            return -1
    
    return sumador

def dividir(num1:float,num2:float)->float:
    """Recibe 2 parametros, numeros tipo float y los divide, retorna el resultado.

    Args:
        num1 (float): dividendo
        num2 (float): divisor

    Returns:
        float: resultado de la division
    """
    if num2 == 0:
        return 0
    else:
        return num1 / num2
    

def contar_heroes(list:list)->int:
    """Recibe la lista de heroes y cuenta la cantidad de heroes que hay y retorna ese contador.

    Args:
        list (list): lista de heroe

    Returns:
        int: cantidad de heroes.
    """
    contador = 0
    for heroes in list:
        contador += 1
    
    return contador

def calcular_promedio(list:list,key:str)->float:
    """Recibe la lista de heroes, la key. Calcula el promedio total de esa key de los heroes.

    Args:
        list (list): lista de heroes
        key (str): key donde calcular el promedio de todos los heroes

    Returns:
        float: retorna el promedio
    """
    cantidad_heroes = contar_heroes(list)
    suma_total = sumar_dato_heroe(list,key)
    promedio = dividir(suma_total,cantidad_heroes)

    return promedio


def stark_calcular_imprimir_promedio_altura(list:list)->float:
    """Recibe la lista de heroes, imprime la altura promedio de los heroes. retorna la altura promedio float

    Args:
        list (list): lista de heroes

    Returns:
        float: retorna la altura promedio
    """
    if len(list) == 0:
        return -1
    
    promedio = calcular_promedio(list,"altura")
    imprimir_dato(f"La altura promedio es {promedio}")
    return promedio



    

def validar_entero(string:str)->bool:
    """Valida si un string recibido por parametro representa un numero entero

    Args:
        string (str): string a validar

    Returns:
        bool: True si es un entero positivo, False si no lo es.
    """
    
    return string.isdigit()



def proyectar_heroe(lista: list, valor: str) -> list:
    """Recibe una lista de heroes, y la key. Retorna una lista solo con los elementos de la key de cada heroe.

    Args:
        lista (list): lista de heroe
        valor (str): key de heroe

    Returns:
        list: lista de elementos de la key.
    """
    lista_nueva = []
    for item in lista:
        lista_nueva.append(item[valor])
    return lista_nueva

def mostrar_heroe(lista: list, titulo: str) -> None:
    """Recibe una lista de heroes y un titulo, imprime el titulo e imprime los heroes de la lista.

    Args:
        lista (list): lista de heroes
        titulo (str): _description_
    """
    print(titulo)
    print("------------------------------")
    for item in lista:
        print(item)

# def proyectar_heroes(lista: list, valor: str, valor_2: str = None) -> list:
#     lista_nueva = []
#     for item in lista:
#         dic = {}
#         if not valor_2 == None:
#             dic[valor] = item[valor]
#             dic[valor_2] = item[valor_2]
#             lista_nueva.append(dic)
#         else:
#             lista_nueva.append(item[valor])
#     return lista_nueva

# def mostrar_heroes(lista: list, titulo: str, valor: str = None, valor_2: str = None) -> None:
#     if not(valor == None and valor_2 == None):
#         print(titulo)
#         print("----------------")
#         for item in lista:
#             print(f'{item[valor]:20s} {item[valor_2]}')
#     else:
#         print(titulo)
#         print("------------------------------")
#         for item in lista:
#             print(item)


def filtrar_lista(lista: list, key: str, valor: str) -> list:
    """Filtra la lista de heroes por la key que recibe por parametro.

    Args:
        lista (list): lista de heroes
        key (str): key a filtrar
        valor (str): criterio

    Returns:
        list: lista filtrada
    """
    lista_filtrada = []
    for value in lista:
        if value[key] == valor:
            lista_filtrada.append(value)
    
    return lista_filtrada


def cantidad_heroes_color_ojos(lista_personajes:list)->None:
    """Recibe la lista de heroes, imprime la cantidad de heroes que tiene cada tipo de color de ojos

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


    for value in contador_de_colores:
        cantidad = contador_de_colores[value]
        print(f"Color {value}: {cantidad}")




def cantidad_heroes_color_pelo(lista_personajes:list)->None:
    """Recibe la lista de heroes, imprime la cantidad de heroes que tiene cada tipo de color de pelo

    Args:
        lista_personajes (list): _description_
    """
    contador_de_colores = {}
    for i in range (len(lista_personajes)):
        color_pelo = lista_personajes[i]["color_pelo"]
        if color_pelo in contador_de_colores:
            contador_de_colores[color_pelo] += 1
        else:
            contador_de_colores[color_pelo] = 1

    for value in contador_de_colores:
        cantidad = contador_de_colores[value]
        print(f"Color {value}: {cantidad}")





def cantidad_heroes_inteligencia(lista_personajes:list)->None:
    """Recibe la lista de heroes, imprime la cantidad de heroes que tiene cada tipo de inteligencia

    Args:
        lista_personajes (list): _description_
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
        
        
    for value in contador_de_inteligencia:
        cantidad = contador_de_inteligencia[value]
        print(f"Tipo {value}: {cantidad}")


def heroes_color_ojos(lista_personajes:list)->None:
    """Imprime los nombres de los heroes por tipo de color de ojo

    Args:
        lista_personajes (list): lista de heroe
    """
    lista_sin_repetir = []
    for value in lista_personajes:
        color_ojos = value["color_ojos"]
        if not color_ojos in lista_sin_repetir:
            lista_sin_repetir.append(color_ojos)
    print(lista_sin_repetir)

    for value in range(len(lista_sin_repetir)):
        print("__________________")
        print(f"*******{lista_sin_repetir[value]}*******")
        print("___________________")
        for valor in lista_personajes:
            if valor["color_ojos"] == lista_sin_repetir[value]:
                print(valor["nombre"])








def imprimir_menu():
    
        # Mostrar menú de opciones
    print("Menú de opciones:")
    print("0. Normalizar Datos")
    print("1. Imprimir nombre de los heroes")
    print("2. Imprimir nombre y altura de los heroes")
    print("3. Buscar superheroe mas alto")
    print("4. Buscar superheroe mas bajo")
    print("5. Promedio de altura de los heroes")
    print("6. Nombre del heroe mas alto y mas bajo")
    print("7. Super heroe mas pesado ")
    print("8. Super heroe mas liviano ")
    print("9. Salir")

def imprimir_menu_02():
    print("0. Normalizar Datos")
    print("1.Imprimir superheroes de genero masculino")
    print("2.Imprimir superheroes de genero femenino")
    print("3.SuperHeroe mas alto masculino")
    print("4.SuperHeroe mas alto femenino")
    print("5.SuperHeroe mas bajo masculino")
    print("6.SuperHeroe mas bajo femenino")
    print("7.Altura promedio de SuperHeroes masculinos")
    print("8.Altura promedio de SuperHeroes femeninos")
    print("9.Nombre de los SuperHeroes asociado a cada uno de los indicadores anteriores")
    print("10.Cantidad SuperHeroes tienen cada tipo de color de ojos")
    print("11.Cantidad SuperHeroes tienen cada tipo de color de pelo")
    print("12.Determinar cuantos SuperHeroes tienen cada tipo de inteligencia")
    print("13.Listar todos los SuperHeroes agrupados por color de ojos")
    print("14.Listar todos los SuperHeroes agrupados por color de pelo")
    print("15.Listar todos los SuperHeroes agrupados por tipo de inteligencia")
    print("16.Salir")
    


    
def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    if validar_entero(opcion):
        return opcion
    else:
        return -1
    
def stark_menu_principal_2():
    imprimir_menu_02()
    opcion = input("Ingrese una opcion: ")
    if validar_entero(opcion):
        return opcion
    else:
        return -1
    

def heroes_color_pelo(lista_personajes:list):
    """lista los heroes con su respectivo color de pelo, imprime por pantalla

    Args:
        lista_personajes (list): lista de heroes
    """
    lista_sin_repetir = []
    for value in lista_personajes:
        color_pelo = value["color_pelo"]
        if not color_pelo in lista_sin_repetir:
            lista_sin_repetir.append(color_pelo)
    print(lista_sin_repetir)


    for value in range(len(lista_sin_repetir)):
        print("__________________")
        print(f"*******Los heroes con el color de pelo {lista_sin_repetir[value]} son*******")
        print("___________________")
        for valor in lista_personajes:
            if valor["color_pelo"] == lista_sin_repetir[value]:
                print(valor["nombre"])


def heroes_inteligencia(lista_personajes:list)->None:
    """Lista los heroes segun el tipo de inteligencia

    Args:
        lista_personajes (list): lista de heroe
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


    
def stark_marvel_app(lista):
    
    while True:
        
        opcion = int(stark_menu_principal())


        while opcion == -1 or opcion < 0 or opcion > 9:
            print("Por favor ingrese una opcion valida:")
            input("Pulse cualquier boton...")
            opcion = int(stark_menu_principal())

        match opcion:
            case 0:
                os.system('cls')
                print("Ha seleccionado la Opción 0")
                stark_normalizar_datos(lista)
                input("Pulse cualquier boton...")
                os.system('cls')
            case 1:
                os.system('cls')
                print("Ha seleccionado la Opción 1")
                stark_imprimir_nombres_heroes(lista)
                input("Pulse cualquier boton...")
                os.system('cls')
                
            case 2:
                os.system('cls')
                print("Ha seleccionado la Opción 2")
                stark_imprimir_nombres_alturas(lista)
                input("Pulse cualquier boton...")
                os.system('cls')
            case 3:
                os.system('cls')
                print("Ha seleccionado la Opción 3")
                stark_calcular_imprimir_heroe(lista,"maximo","altura")
                
                input("Pulse cualquier boton...")
                os.system('cls')
            case 4:
                os.system('cls')
                print("Ha seleccionado la Opción 4")
                stark_calcular_imprimir_heroe(lista,"minimo","altura")
                
                input("Pulse cualquier boton...")
                os.system('cls')
            case 5:
                os.system('cls')
                print("Ha seleccionado la Opción 5")
                stark_calcular_imprimir_promedio_altura(lista)
                input("Pulse cualquier boton...")
                os.system('cls')
            case 6:
                os.system('cls')
                print("Ha seleccionado la Opción 6")
                stark_calcular_imprimir_heroe(lista, "maximo", "altura")
                stark_calcular_imprimir_heroe(lista,"minimo","altura")
                input("Pulse cualquier boton...")
                os.system('cls')
            case 7:
                os.system('cls')
                print("Ha seleccionado la Opción 7")
                stark_calcular_imprimir_heroe(lista, "maximo", "peso")
                input("Pulse cualquier boton...")
                os.system('cls')
            case 8:
                os.system('cls')
                print("Ha seleccionado la Opción 8")
                stark_calcular_imprimir_heroe(lista, "minimo", "peso")
                input("Pulse cualquier boton...")
                os.system('cls')
            case 9:
                print("Saliendo del programa...")
                input("Presione cualquier tecla...")
                break
            case _:
                print("Opción inválida. Por favor, seleccione una opción válida.")



def stark_marvel_app_2(lista):
    
    while True:
        
        opcion = int(stark_menu_principal_2())


        while opcion == -1 or opcion < 0 or opcion > 16:
            print("Por favor ingrese una opcion valida:")
            input("Pulse cualquier boton...")
            opcion = int(stark_menu_principal_2())

        match opcion:
            case 0:
                os.system('cls')
                print("Ha seleccionado la Opción 0")
                stark_normalizar_datos(lista)
                input("Pulse cualquier boton...")
                os.system('cls')
            case 1:
                os.system('cls')
                mostrar_heroe(proyectar_heroe(filtrar_lista(lista, "genero", "M"), "nombre"), "Los heroes masculinos son: ")
                input("Pulse cualquier boton...")
                os.system('cls')

            case 2:
                os.system('cls')
                mostrar_heroe(proyectar_heroe(filtrar_lista(lista, "genero", "F"), "nombre"), "Los heroes femeninos son: ")
                input("Pulse cualquier boton...")
                os.system('cls')
            case 3:
                os.system('cls')
                stark_calcular_imprimir_heroe(filtrar_lista(lista, "genero", "M"), "maximo", "altura")
                input("Pulse cualquier boton...")
                os.system('cls')
            case 4:
                os.system('cls')
                stark_calcular_imprimir_heroe(filtrar_lista(lista, "genero", "F"), "maximo", "altura")
                input("Pulse cualquier boton...")
                os.system('cls')
            case 5:
                os.system('cls')
                stark_calcular_imprimir_heroe(filtrar_lista(lista, "genero", "M"), "minimo", "altura")
                input("Pulse cualquier boton...")
                os.system('cls')
            case 6:
                os.system('cls')
                stark_calcular_imprimir_heroe(filtrar_lista(lista, "genero", "F"), "minimo", "altura")
                input("Pulse cualquier boton...")
                os.system('cls')
            case 7:
                os.system('cls')
                stark_calcular_imprimir_promedio_altura(filtrar_lista(lista,"genero","M"))
                input("Pulse cualquier boton...")
                os.system('cls')
            case 8:
                os.system('cls')
                stark_calcular_imprimir_promedio_altura(filtrar_lista(lista,"genero","F"))
                input("Pulse cualquier boton...")
                os.system('cls')
            case 9:
                os.system('cls')
                stark_calcular_imprimir_heroe(filtrar_lista(lista, "genero", "M"), "maximo", "altura")
                stark_calcular_imprimir_heroe(filtrar_lista(lista, "genero", "F"), "maximo", "altura")
                stark_calcular_imprimir_heroe(filtrar_lista(lista, "genero", "M"), "minimo", "altura")
                stark_calcular_imprimir_heroe(filtrar_lista(lista, "genero", "F"), "minimo", "altura")
                input("Pulse cualquier boton...")
                os.system('cls')
            case 10:
                os.system('cls')
                cantidad_heroes_color_ojos(lista)
                input("Pulse cualquier boton...")
                os.system('cls')
            case 11:
                os.system('cls')
                cantidad_heroes_color_pelo(lista)
                input("Pulse cualquier boton...")
                os.system('cls')
            case 12:
                os.system('cls')
                cantidad_heroes_inteligencia(lista)
                input("Pulse cualquier boton...")
                os.system('cls')
            case 13:
                os.system('cls')
                heroes_color_ojos(lista)
                input("Pulse cualquier boton...")
                os.system('cls')
            case 14:
                os.system('cls')
                heroes_color_pelo(lista)
                input("Pulse cualquier boton...")
                os.system('cls')
            case 15:
                os.system('cls')
                heroes_inteligencia(lista)
                input("Pulse cualquier boton...")
                os.system('cls')
            case 16:
                print("Saliendo del programa...")
                input("Presione cualquier tecla...")
                break
            case _:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    


def stark_marvel_app_principal(lista):
    entrada = True
    while entrada:
        os.system("cls")
        print("Elija un menu:")
        print("1.Marvel Stark 01")
        print("2.Marvel Stark 02")
        print("3.Salir")

        opcion = input()
        match opcion:
            case "1":
                os.system("cls")
                print("Entrando...")
                input("Precione cualquier tecla...")
                os.system("cls")
                stark_marvel_app(lista)
                os.system("cls")

            case "2":
                os.system("cls")
                print("Entrando...")
                input("Precione cualquier tecla...")
                os.system("cls")
                stark_marvel_app_2(lista)
                os.system("cls")

            case "3":
                os.system("cls")
                input("Saliendo...precione cualquier tecla")
                break

            case _:
                input("Opcion invalida...ingrese una opcion valida...")
