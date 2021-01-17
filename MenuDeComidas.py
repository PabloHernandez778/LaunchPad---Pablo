import os

#Menu principal
def menu2():
    os.system('cls')
    print("\t   --MENU PRINCIPAL--")
    print("\tSelecciona una opcion")
    print("\t1 - Snack")
    print("\t2 - Desayuno ")
    print("\t3 - Almuerzo")
    print("\t4 - Cena")

#Menu Snack
def snack_opciones():
    os.system('cls')
    print("\t     --MENU SNACK--")
    print("\t  Selecciona una opcion")
    print("\t1 - Insertar nueva comida")
    print("\t2 - Ver comidas")
    print("\t3 - Salir")
    while True:
        opcion_snack_opciones = input("Digita la opcion que desea >> \n")
        if opcion_snack_opciones == '1':
            snack_insetrar()
        elif opcion_snack_opciones == '2':
            snack_ver()
        elif opcion_snack_opciones == '3':
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...")

#SubMenu para insertar nuevos snacks
def snack_insetrar():
    os.system('cls')
    archivo = open ("../txt/Snack.txt", "a")
    nombre = input("Digite el nombre del Snack: \n")
    archivo.write("Nombre: " + nombre + '\n')
    ingredientes = input("Introduce los ingredientes del Snack: \n ")
    archivo.write("Ingredientes: "+ ingredientes + '\n')
    instrucciones = input("Digita las instruucciones de preparacion: \n")
    archivo.write("Instrucciones: "+ instrucciones + '\n')
    print('\n')

def snack_ver():
    os.system('cls')
    archivo_uno = open("../txt/Snack.txt")
    print(archivo_uno.read())

#Menu Desayuno
def desayuno_opciones():
    os.system('cls')
    print("\t   --MENU DESAYUNO--")
    print("\t Selecciona una opcion")
    print("\t1 - Insertar nueva comida")
    print("\t2 - Ver comidas")
    print("\t3 - Salir")
    while True:
        opcion_desayuno_opciones = input("Digita la opcion que desea >> \n")
        if opcion_desayuno_opciones == '1':
            desayuno_insertar()
        elif opcion_desayuno_opciones == '2':
            desayuno_ver()
        elif opcion_desayuno_opciones == '3':
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...")

#SubMenu de Desayuno para agregar
def desayuno_insertar():
    os.system('cls')
    archivo_desayuno = open("Desayuno.txt", "a")
    nombre_desayuno = input("Digite el nombre del Desayuno: \n")
    archivo_desayuno.write("Nombre: " + nombre_desayuno + '\n')
    ingredientes_desayuno = input("Introduce los ingredientes del Desayuno: \n ")
    archivo_desayuno.write("Ingredientes: " + ingredientes_desayuno + '\n')
    instrucciones_desayuno = input("Digita las instruucciones de preparacion: \n")
    archivo_desayuno.write("Instrucciones: " + instrucciones_desayuno + '\n')
    print('\n')

#SubMenu para ver los desayunos que hay
def desayuno_ver():
    os.system('cls')
    archivo_dos = open("Desayuno.txt")
    print(archivo_dos.read())

#Menu de Almuerzo
def almuerzo_opciones():
    os.system('cls')
    print("\t    --MENU ALMUERZO--")
    print("\t Selecciona una opcion")
    print("\t1 - Insertar nueva comida")
    print("\t2 - Ver comidas")
    print("\t3 - Salir")
    while True:
        opcion_almuerzo_opciones = input("Digita la opcion que desea >> \n")
        if opcion_almuerzo_opciones == '1':
            almuerzo_insertar()

        elif opcion_almuerzo_opciones == '2':
            almuerzo_ver()

        elif opcion_almuerzo_opciones == '3':
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...")

def almuerzo_insertar():
    os.system('cls')
    archivo_almuerzo = open("Almuerzo.txt", "a")
    nombre_almuerzo = input("Digite el nombre del Almuerzo: \n")
    archivo_almuerzo.write("Nombre: " + nombre_almuerzo + '\n')
    ingredientes_almuerzo = input("Introduce los ingredientes del Almuerzo: \n ")
    archivo_almuerzo.write("Ingredientes: " + ingredientes_almuerzo + '\n')
    instrucciones_almuerzo = input("Digita las instruucciones de preparacion: \n")
    archivo_almuerzo.write("Instrucciones: " + instrucciones_almuerzo + '\n')
    print('\n')

#SubMenu para ver los Almuerzos
def almuerzo_ver():
    os.system('cls')
    archivo_tres = open("Almuerzo.txt")
    print(archivo_tres.read())

#Menu Cena
def cena_opciones():
    os.system('cls')
    print("\t     --MENU CENA--")
    print("\t  Selecciona una opcion")
    print("\t1 - Insertar nueva comida")
    print("\t2 - Ver comidas")
    print("\t3 - Salir")
    while True:
        opcion_cena_opciones = input("Digita la opcion que desea >> \n")
        if opcion_cena_opciones == '1':
            cena_insertar()
        elif opcion_cena_opciones == '2':
            cena_ver()
        elif opcion_cena_opciones == '3':
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...")

#SubMenu para insertar platos de Cena
def cena_insertar():
    os.system('cls')
    archivo_cena = open("Cena.txt", "a")
    nombre_cena = input("Digite el nombre de la Cena: \n")
    archivo_cena.write("Nombre: " + nombre_cena + '\n')
    ingredientes_cena = input("Introduce los ingredientes de la Cena: \n ")
    archivo_cena.write("Ingredientes: " + ingredientes_cena + '\n')
    instrucciones_cena = input("Digita las instruucciones de preparacion: \n")
    archivo_cena.write("Instrucciones: " + instrucciones_cena + '\n')
    print('\n')
#SubMenu para ver los platos de Cena
def cena_ver():
    os.system('cls')
    archivo_cuatro = open("Cena.txt")
    print(archivo_cuatro.read())

#Ciclo while para validar las teclas
while True:
    # Mostramos el menu
    menu2()
    #Opciones para el usuario
    opcionMenu2 = input("Digita la opcion que desea >> ")

    if opcionMenu2 == "1":
        snack_opciones()

    elif opcionMenu2 == "2":
        desayuno_opciones()

    elif opcionMenu2 == "3":
        almuerzo_opciones()

    elif opcionMenu2 == "4":
        cena_opciones()

    elif opcionMenu2 == "4":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...")