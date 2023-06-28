#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe

def imprimir_heroes(lista:list)->None:
    """Recorre la lista imprimiendo por consola el nombre de cada superhéroe

    Args:
        lista (list): lista de heroes
    """
    for nombres in range(len(lista)):
        print(lista[nombres]["nombre"])

#Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def imprimir_heroe_altura(lista:list)->None:
    """Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo

    Args:
        lista (list): lista de heroe
    """
    print("Nombre\t\t\tAltura")
    for datos in range(len(lista)):
        print(f'{lista[datos]["nombre"]:23s} {float(lista[datos]["altura"]):.2f}')

# Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def heroe_mas_alto(lista:list)->tuple:
    """Recorre la lista y determinar cuál es el superhéroe más alto (MÁXIMO)

    Args:
        lista (list): lista de heroes
    """
    altura_mas_alta = 0.0
    for alturas in range(len(lista)):
        altura = float(lista[alturas]["altura"])
        if altura > altura_mas_alta:
            altura_mas_alta = altura
            nombre_altura_alta = lista[alturas]["nombre"]
    
    return(nombre_altura_alta, altura_mas_alta)

#Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def heroe_mas_bajo(lista:list)->tuple:
    """Recorre la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

    Args:
        lista (list): lista de heroe

    Returns:
        tuple: retorna el nombre y la altura mas baja
    """
    altura_mas_baja = 0.0
    flag_altura = True
    for alturas in range(len(lista)):
        altura = float(lista[alturas]["altura"])
        if altura < altura_mas_baja or flag_altura == True:
            altura_mas_baja = altura
            nombre_altura_baja = lista[alturas]["nombre"]
            flag_altura = False

    return(nombre_altura_baja,altura_mas_baja)

# Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)

def heroe_altura_promedio(lista:list)->float:
    """Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)

    Args:
        lista (list): lista de heroes

    Returns:
        float: retorna el promedio
    """
    sumador = 0
    contador = 0
    for alturas in range(len(lista)):
        sumador += float(lista[alturas]["altura"])
        contador += 1
    promedio = sumador / contador
    return(promedio)


# Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)

def heroe_buscar_identidad(nombre:str,lista:list)->str:
    """Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)

    Args:
        nombre (str): nombre del heroe
        lista (list): lista de heroes

    Returns:
        str: retorna la identidad del heroe
    """
    for i in range(len(lista)):
        if nombre == lista[i]["nombre"]:
            identidad = lista[i]["identidad"]
            
    return(identidad)

# Calcular e informar cual es el superhéroe más y menos pesado.
def heroe_mas_y_menos_pesado(lista:list)->tuple:
    """ Calcula e informa cual es el superhéroe más y menos pesado.

    Args:
        lista (list): lista de heroe

    Returns:
        tuple: retorna una tupla que contiene los datos 
    """
    heroe_mas_pesado = 0.0
    heroe_menos_pesado= 0.0
    flag_heroe_menos_pesado = True
    for peso in range(len(lista)):
        
        if heroe_mas_pesado < float(lista[peso]["peso"]):
            heroe_mas_pesado = float(lista[peso]["peso"])
            nombre_heroe_mas_pesado = lista[peso]["nombre"]

        if flag_heroe_menos_pesado == True or heroe_menos_pesado > float(lista[peso]["peso"] ):
            heroe_menos_pesado = float(lista[peso]["peso"])
            nombre_heroe_menos_pesado = lista[peso]["nombre"]
            flag_heroe_menos_pesado = False
    return(nombre_heroe_mas_pesado, heroe_mas_pesado, nombre_heroe_menos_pesado, heroe_menos_pesado )


# Construir un menú que permita elegir qué dato obtener

def menu_00()->int:
    """Menu que pide un opcion al usuario y luego la retorna como entero

    Returns:
        int: retorna la opcion ingresada por el usuario como entero
    """
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Imprimir nombre de los heroes")
    print("2. Imprimir nombre y altura de los heroes")
    print("3. Buscar superheroe mas alto")
    print("4. Buscar superheroe mas bajo")
    print("5. Promedio de altura de los heroes")
    print("6. Identidad del heroe mas alto o mas bajo")
    print("7. Super heroe mas pesado y menos pesado")
    print("8. Salir")
    print("0.Siguiente menu")
    
    opcion = int(input("\nIngrese la opción deseada: "))

    return opcion


    
    


