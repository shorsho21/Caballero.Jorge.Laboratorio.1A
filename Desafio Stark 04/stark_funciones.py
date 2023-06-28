import os

def extraer_iniciales(nombre_heroe:str)->str:
    """Recibe como parametro el nombre del personaje y extrae los iniciales y lo retorna, si la lista esta vacia retorna N/A

    Args:
        nombre_heroe (str): nombre del heroe

    Returns:
        _type_: str
    """

    if len(nombre_heroe) == 0:
        return "N/A"

    nombre_heroe = nombre_heroe.replace("-", " ")

    palabras = nombre_heroe.split()
    iniciales = ""
    for palabra in palabras:
        if palabra != "The" and palabra != "the":
            iniciales += palabra[0].upper() + "."

    return iniciales


def definir_iniciales_nombre(heroe:dict)->bool:
    """Recibe un diccionario con los datos de un heroe, agrega al diccionario la key iniciales con sus iniciales
    retorna True si se pudo realizar, retorna False si no se pudo realizar

    Args:
        heroe (_type_): dict

    Returns:
        _type_: Bool
    """
    if type(heroe) != dict or "nombre" not in heroe:
        return False

    heroe["iniciales"] = extraer_iniciales(heroe["nombre"])

    return True


def agregar_iniciales_nombre(lista_heroes:list)->bool:
    """Recibe como parametro la lista de personajes, itera la lista, agrega al diccionario de cada heroe la key iniciales con sus iniciales
    retorna True si se realizo y False si no se pudo

    Args:
        lista_heroes (list): lista de personajes heroes

    Returns:
        _type_: Bool
    """
    if type(lista_heroes) != list or len(lista_heroes) < 0:
        return False

    for heroes in range(len(lista_heroes)):
        comprobacion = definir_iniciales_nombre(lista_heroes[heroes])
        if comprobacion == False:
            print("El origen de datos no contiene el formato correcto")
            return False

    return True


def stark_imprimir_nombres_con_iniciales(lista_heroes:list)->None:
    """Recibe la lista de heroes y luego los imprime junto con sus iniciales

    Args:
        lista_heroes (list): lista de heroes

    Returns:
        _type_: none
    """
    if type(lista_heroes) != list or len(lista_heroes) < 0:
        return False

    agregar_iniciales_nombre(lista_heroes)

    for heroe in lista_heroes:
        print(f"* {heroe['nombre']} ({heroe['iniciales']})")


def generar_codigo_heroe(id_heroe:int, genero_heroe:str)->str:
    """Recibe id del heroe, y el genero por parametro y devuelve un codigo de heroe

    Args:
        id_heroe (int): id del heroe
        genero_heroe (str): genero del heroe

    Returns:
        str: codigo del heroe
    """
    generos_esperados = ["M", "F", "NB"]
    codigo_heroe = ""
    if type(id_heroe) != int or genero_heroe.upper() not in generos_esperados:
        return "N/A"

    contador = (9 - len(str(id_heroe))) - len(genero_heroe)
    cero = ""
    if contador < 0:
        return "N/A"

    for ceros in range(contador):
        cero += "0"

    codigo_heroe = f"{genero_heroe}-{cero}{id_heroe}"

    return codigo_heroe


def agregar_codigo_heroe(heroe:dict, id_heroe:int)->bool:
    """Recibe por parametro un diccionario de un heroe y la id de un heroe, agrega una nueva clave al diccionario codigo_heroe con el
    codigo del heroe

    Args:
        heroe (dict): Diccionario del heroe
        id_heroe (int): id del heroe

    Returns:
        _type_: Bool
    """
    if len(heroe) == 0:
        return False
    if len(generar_codigo_heroe(id_heroe, heroe["genero"])) == 10:
        heroe["codigo_heroe"] = generar_codigo_heroe(id_heroe, heroe["genero"])

        return True
    else:
        return False


def stark_generar_codigos_heroes(lista_heroes:list)->None:
    """Recibe la lista de heroes, luego genera y agrega a cada diccionario del heroe un codigo_heroe

    Args:
        lista_heroes (list): Lista de heroes
    """
    if len(lista_heroes) == 0:
        print("El origen de datos no contiene el formato correcto")

    contador = 0
    for heroes in range(len(lista_heroes)):
        if type(lista_heroes[heroes]) == dict and "genero" in lista_heroes[heroes]:
            agregar_codigo_heroe(lista_heroes[heroes], heroes+1)
            contador += 1
        else:
            print("El origen de datos no contiene el formato correcto")

    print(f"Se asignaron {contador} codigos")
    print(f"El codigo del primer heroe es: {lista_heroes[0]['codigo_heroe']}")
    print(
        f"El codigo del ultimo heroe es: {lista_heroes[contador-1]['codigo_heroe']}")


# def sanitizar_entero(numero_str):

#     try:

#         numero = int(numero_str)
#         if numero < 0:
#             return -2
#         else:
#             return numero

#     except ValueError:
#         return -1
#     except:
#         return -3

def sanitizar_entero(numero_str:str)->int:
    """Recibe un string que puede representar un entero y determina si el numero es entero positivo, si se cumple retorna el numero
    como entero.

    Args:
        numero_str (_type_): _description_

    Returns:
        int: retorna el numero str  como entero
    """
    numero_str = numero_str.strip()  # Eliminar espacios en blanco al inicio y al final

    if any(char.isalpha() for char in numero_str):
        return -1

    if numero_str[1:].isdigit() and numero_str[0] == "-":
        return -2

    if numero_str.isdigit():
        return int(numero_str)
    elif numero_str.replace(".", "", 1).isdigit():
        if float(numero_str) < 0:
            return -3
        else:
            return -3
    else:
        return -2


# PENDIENTE
def sanitizar_flotante(numero_str:str)->float:
    """Recibe un posible numero flotante en str y si es positivo flotante lo retorna como float.

    Args:
        numero_str (_type_): numero flotante str

    Returns:
        _type_: float
    """
    numero_str = numero_str.strip()
    prueba = numero_str
    try:
        if any(char.isalpha() for char in numero_str):
            return -1
        int(prueba)
        return -3

    except ValueError:
        numero = float(numero_str)
        if numero < 0:
            return -2
        else:
            return numero
    except:
        return -3


def sanitizar_string(valor_str:str, valor_por_defecto:str)->str:
    """Recibe un string y determina si es solo texto, si se cumple retorna el string en minusculas, si no se cumple retorna N/A

    Args:
        valor_str (str): string a validar
        valor_por_defecto (str): -

    Returns:
        _type_: str
    """

    valor_str = valor_str.strip()
    valor_str = valor_str.replace('/', ' ')
    valor_defecto = valor_por_defecto.strip()

    if len(valor_str) == 0:
        return valor_defecto.lower()

    if any(char.isdigit() for char in valor_str):
        return 'N/A'
    else:
        return valor_str.lower()


def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str)->bool:
    """Recibe por parametro un diccionario de un heroe, la key del diccionario y el tipo de dato a sanitizar, si se pudo sanitizar
    entonces retorna True, caso contrario retorna False

    Args:
        heroe (dict): diccionario del heroe
        clave (str): key del diccionario del heroe
        tipo_dato (str): tipo de dato a sanitizar

    Returns:
        bool: True si se pudo, False si no se pudo
    """

    if sanitizar_string(tipo_dato, "-") == "N/A" or sanitizar_string(tipo_dato, "-") == "-":
        return print("Tipo de dato no reconocido")

    if not clave in heroe:
        return print("La clave especificada no existe en el heroe")

    if tipo_dato == "string":
        if sanitizar_string(heroe[clave], "-") == "N/A" or sanitizar_string(heroe[clave], "-") == "-":
            return False
        else:
            heroe[clave] = sanitizar_string(heroe[clave], "-")
            return True
    elif tipo_dato == "entero":
        if sanitizar_entero(heroe[clave]) == -1 or sanitizar_entero(heroe[clave]) == -2 or sanitizar_entero(heroe[clave]) == -3:
            return False
        else:
            heroe[clave] = sanitizar_entero(heroe[clave])
            return True

    elif tipo_dato == "flotante":
        if type(sanitizar_flotante(heroe[clave])) == float:
            heroe[clave] = sanitizar_flotante(heroe[clave])
            return True
        else:
            return False


def stark_normalizar_datos(lista_heroes:list)->None:
    """Recibe la lista de heroes y sanitiza todos los datos de los heroes.

    Args:
        lista_heroes (list): lista de heroes

    Returns:
        _type_: none
    """
    if len(lista_heroes) == 0:
        print("Error, La lista de heroes vacia")
        return False

    for heroes in range(len(lista_heroes)):
        sanitizar_dato(lista_heroes[heroes],"altura","flotante")
        sanitizar_dato(lista_heroes[heroes],"peso","flotante")
        sanitizar_dato(lista_heroes[heroes],"color_ojos","string")
        sanitizar_dato(lista_heroes[heroes],"color_pelo","string")
        sanitizar_dato(lista_heroes[heroes],"fuerza","entero")
        sanitizar_dato(lista_heroes[heroes],"inteligencia","string")
    print("Datos normalizados")

def generar_indice_nombres(lista_heroes:list)->list:
    """Recibe por parametro la lista de heroes y retorna una lista con los nombres de los heroes

    Args:
        lista_heroes (list): _description_

    Returns:
        list: lista de indice de nombres
    """
    lista_indice_nombres = []
    if len(lista_heroes) == 0:
        print("El origen de datos no contiene el formato correcto")
        return None
    
    for heroes in lista_heroes:
        if type(heroes) != dict:
            return None
        
        if "nombre" not in heroes:
            print("El origen de datos no contiene el formato correcto")
            return None
    
        nombre = heroes["nombre"]
        nombre_dividido = nombre.split()
        lista_indice_nombres.extend(nombre_dividido)
    
    return lista_indice_nombres


def stark_imprimir_indice_nombre(lista_heroes:list)->None:
    """Recibe la lista de heroes e imprime el indice de nombres separados por un guion

    Args:
        lista_heroes (list): lista de heroes
    """
    lista_indice_heroes = generar_indice_nombres(lista_heroes)
    separador = "-"
    resultado = separador.join(lista_indice_heroes)
    print(resultado)
    print(type(resultado))


def convertir_cm_a_mtrs(valor_cm:float)->float:
    """Recibe un valor en centimentros tipo float y lo transforma en metros tipo float

    Args:
        valor_cm (float): valor en cm

    Returns:
        float: retorna el valor en unidades metro
    """
    if valor_cm != float or valor_cm < 0:
        return -1
    
    valor_metros = valor_cm / 100

    return valor_metros

def generar_separador(patron:str,largo:int,imprimir:bool = True)->str:
    """Recibe un patron que es un solo caracter, el largo las veces que se repite, y un bool si se imprime o no por pantalla

    Args:
        patron (str): caracter 
        largo (int): cantidad que se repite el patron
        imprimir (bool, optional): Si esta en True se imprime antes de retornar, en False no imprime solo retorna. Defaults to True.

    Returns:
        str: retorna el patron repetido por la cantidad que se recibio por parametro
    """
    if len(patron) <0 or len(patron) > 2:
        return "N/A"
    elif largo < 0 or largo > 235:
        return "N/A"
    
    separador = ""
    for patrones in range(largo):
        separador += patron

    if imprimir == False:
        return separador
    
    elif imprimir == True:
        print(separador)
        return separador
    else:
        return "N/A"

    
def generar_encabezado(titulo:str)->str:
    """Genera e imprime un encabezado con un titulo recibido por parametro

    Args:
        titulo (str): El titulo para el encabezado a imprimir

    Returns:
        str: Retorna el encabezado generado
    """
    titulo_mayuscula = titulo.upper()
    separador = "******************************"
    
    encabezado = f"{separador}\n{titulo_mayuscula}\n{separador}"

    return encabezado


def imprimir_ficha_heroe(heroe:dict)->None:
    """Imprime una ficha con los datos del diccionario del heroe recibido por parametro

    Args:
        heroe (dict): Diccionario del heroe
    """

    generar_encabezado("principal")

    print(f"NOMBRE DEL HEROE:            {heroe['nombre']} ({heroe['iniciales']})")
    print(f"IDENTIDAD SECRETA:           {heroe['identidad']}")
    print(f"CONSULTORA:                  {heroe['empresa']}")
    print(f"CODIGO DE HEROE              {heroe['codigo_heroe']}")

    generar_encabezado("fisico")
    print(f"ALTURA:                      {heroe['altura']:.4}")
    print(f"PESO                         {heroe['peso']:.4}")
    print(f"FUERZA                       {heroe['fuerza']}")

    generar_encabezado("señas particulares")
    print(f"COLOR DE OJOS                {heroe['color_ojos']}")
    print(f"COLOR DE PELO                {heroe['color_pelo']}")

def stark_navegar_fichas(lista_heroes:list)->None:
    """Imprime la ficha del primer personaje y luego imprime un menu de opciones y pide al usuario que ingrese una opcion

    Args:
        lista_heroes (list): lista de heroes
    """
    pagina = 0
    while True:
        os.system("cls")
        imprimir_ficha_heroe(lista_heroes[pagina])
        opcion= input("[1]Ir a la izquierda   [2]Ir a la derecha  [S]Salir  :")

        if opcion == "1":
            pagina = (pagina - 1) % len(lista_heroes)

        elif opcion == "2":
            pagina = (pagina + 1) % len(lista_heroes)

        elif opcion =="S" or opcion == "s":
            input("Saliendo...Precione cualquier boton...")
            break
        else:
            input("Opcion invalida...Vuelva a intentar...")

def imprimir_menu()->None:
    print("""

1 - Imprimir la lista de nombres junto con sus iniciales
2 - Generar códigos de héroes
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
S - Salir

____________________________________________________________
""")
    
def stark_menu_principal()->None:
    """Imprime el menu de opciones y pide al usuario que ingrese una, la funcion retorna la respuesta del usuario

    Returns:
        _type_: none
    """
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    return opcion






def stark_marvel_app_3(lista:list)->None:
    """La funcion se encarga de la ejecucion principal del programa

    Args:
        lista (list): lista de heroes
    """
    
    while True:
        
        opcion = stark_menu_principal()
        match opcion:

            case "1":
                os.system("cls")
                stark_imprimir_nombres_con_iniciales(lista)
                input("Precione cualquier tecla...")
                os.system("cls")
            case "2":
                os.system("cls")
                stark_generar_codigos_heroes(lista)
                input("Precione cualquier tecla...")
                os.system("cls")
            case "3":
                os.system("cls")
                stark_normalizar_datos(lista)
                input("Precione cualquier tecla...")
                os.system("cls")
            case "4":
                os.system("cls")
                stark_imprimir_indice_nombre(lista)
                input("Precione cualquier tecla...")
                os.system("cls")
            case "5":
                os.system("cls")
                if "codigo_heroe" in lista[0]:
                    stark_navegar_fichas(lista)
                    os.system("cls")
                else:
                    print("Tienes que generar los codigos de heroes primero")
                    input("Precione cualquier tecla...")
                    os.system("cls")
            case "s":
                os.system("cls")
                print("Saliendo del programa...")
                input("Precione cualquier tecla...")
                os.system("cls")
                break

            case _:
                os.system("cls")
                print("El valor no es valido, ingrese un valor valido...")
                input("Precione cualquier tecla para continuar...")
                os.system("cls")
                

            

    









    













