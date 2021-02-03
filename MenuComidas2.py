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
    print("\t  -Selecciona una opcion")
    print("\t1 - Insertar nueva comida")
    print("\t2 - Ver comidas")
    print("\t3 - Salir")
    while True:
        opcion_snack_opciones = input("-Digita la opcion que desea >> \n")
        if opcion_snack_opciones == '1':
            snack_insetrar()
        elif opcion_snack_opciones == '2':
            snack_ver()
        elif opcion_snack_opciones == '3':
            break
        else:
            print("")
            input("-No has pulsado ninguna opción correcta...")

#SubMenu para insertar nuevos snacks
def snack_insetrar():
    Folder_name = "FolderSnacks/"
    if (not os.path.isdir(Folder_name)):
        os.mkdir(Folder_name)

    print("\t     -- INSERTE SNACKS--  ")
    nombre_snack = input("-Digite el nombre del Snack: ")
    SnackFileName = nombre_snack + ".txt"
    CrearSnack = open(Folder_name + SnackFileName, "a")
    CrearSnack.write("-Snack: "+ nombre_snack+ '\n ')
    ingredientes_snack = input("-Introduce los ingredientes del Snack: \n ")
    CrearSnack.write("-Ingredientes: " + ingredientes_snack + '\n')
    instrucciones_snack = input("-Digita las instrucciones de preparacion: \n")
    CrearSnack.write("-Instrucciones: " + instrucciones_snack + '\n')


    print('\n')


def snack_ver():
    print("\t     -- SNACKS--  ")
    Folder_name = "FolderSnacks/"
    Files = os.listdir(Folder_name)
    index = 1
    for f in Files:
        print(index,"-",f)
        index = index +1

    Seleccion = int(input("-Seleccione el Snack: "))
    selected_file = Files[Seleccion-1]
    x = open("FolderSnacks/" + selected_file, "r")
    print(x.read())
    


#Menu Desayuno
def desayuno_opciones():
    os.system('cls')
    print("\t   --MENU DESAYUNO--")
    print("\t -Selecciona una opcion")
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
            input("-No has pulsado ninguna opción correcta...")

#SubMenu de Desayuno para agregar
def desayuno_insertar():
    Folder_name = "FolderDesayuno/"
    if (not os.path.isdir(Folder_name)):
        os.mkdir(Folder_name)
    print("\t     -- INSERTE DESAYUNO --   ")
    nombre_desayuno = input("-Digite el nombre del Desayuno: ")
    DesayunoFileName = nombre_desayuno + ".txt"
    CrearDesayuno = open(Folder_name + DesayunoFileName, "a")
    CrearDesayuno.write("-Snack: " + nombre_desayuno + '\n ')
    ingredientes_desayuno = input("-Introduce los ingredientes del Desayuno: \n ")
    CrearDesayuno.write("-Ingredientes: " + ingredientes_desayuno + '\n')
    instrucciones_desayuno = input("-Digita las instrucciones de preparacion: \n")
    CrearDesayuno.write("-Instrucciones: " + instrucciones_desayuno + '\n')
    print('\n')



#SubMenu para ver los desayunos que hay
def desayuno_ver():
    print("\t     -- DESAYUNOS--   ")
    Folder_name = "FolderDesayuno/"
    Files = os.listdir(Folder_name)
    index = 1
    for f in Files:
        print(index, "-", f)
        index = index + 1

    Seleccion = int(input("-Seleccione el Desayuno: "))
    selected_file = Files[Seleccion - 1]
    x = open("FolderDesayuno/" + selected_file, "r")
    print(x.read())


#Menu de Almuerzo
def almuerzo_opciones():
    os.system('cls')
    print("\t    --MENU ALMUERZO--")
    print("\t -Selecciona una opcion-")
    print("\t1 - Insertar nueva comida")
    print("\t2 - Ver comidas")
    print("\t3 - Salir")
    while True:
        opcion_almuerzo_opciones = input("-Digita la opcion que desea >> \n")
        if opcion_almuerzo_opciones == '1':
            almuerzo_insertar()

        elif opcion_almuerzo_opciones == '2':
            almuerzo_ver()

        elif opcion_almuerzo_opciones == '3':
            break
        else:
            print("")
            input("-No has pulsado ninguna opción correcta...")

def almuerzo_insertar():
    Folder_name = "FolderAlmuerzo/"
    if (not os.path.isdir(Folder_name)):
        os.mkdir(Folder_name)
    print("\t     --INSERTAR ALMUERZO--  ")
    nombre_almuerzo = input("-Digite el nombre del Almuerzo: ")
    AlmuerzoFileName = nombre_almuerzo + ".txt"
    CrearAlmuerzo = open(Folder_name + AlmuerzoFileName, "a")
    CrearAlmuerzo.write("-Almuerzo: " + nombre_almuerzo + '\n ')
    ingredientes_almuerzo = input("-Introduce los ingredientes del Almuerzo: \n ")
    CrearAlmuerzo.write("-Ingredientes: " + ingredientes_almuerzo + '\n')
    instrucciones_almuerzo = input("-Digita las instrucciones de preparacion: \n")
    CrearAlmuerzo.write("-Instrucciones: " + instrucciones_almuerzo + '\n')
    print('\n')


#SubMenu para ver los Almuerzos
def almuerzo_ver():
    print("\t     -- ALMUERZOS --")
    Folder_name = "FolderAlmuerzo/"
    Files = os.listdir(Folder_name)
    index = 1
    for f in Files:
        print(index,"-",f)
        index = index +1

    Seleccion = int(input("-Seleccione el Almuerzo: "))
    selected_file = Files[Seleccion-1]
    x = open("FolderAlmuerzo/" + selected_file, "r")
    print(x.read())




#Menu Cena
def cena_opciones():
    os.system('cls')
    print("\t     --MENU CENA--  ")
    print("\t  -Selecciona una opcion-")
    print("\t1 - Insertar nueva comida")
    print("\t2 - Ver comidas")
    print("\t3 - Salir")
    while True:
        opcion_cena_opciones = input("-Digita la opcion que desea >> \n")
        if opcion_cena_opciones == '1':
            cena_insertar()
        elif opcion_cena_opciones == '2':
            cena_ver()
        elif opcion_cena_opciones == '3':
            break
        else:
            print("")
            input("-No has pulsado ninguna opción correcta...")

#SubMenu para insertar platos de Cena
def cena_insertar():
    Folder_name = "FolderCena/"
    if (not os.path.isdir(Folder_name)):
        os.mkdir(Folder_name)
    print("\t     -- INSERTE CENA --  ")
    nombre_cena = input("-Digite el nombre de la Cena: ")
    CenaFileName = nombre_cena + ".txt"
    CrearCena = open(Folder_name + CenaFileName, "a")
    CrearCena.write("-Cena: " + nombre_cena + '\n ')
    ingredientes_cena = input("-Introduce los ingredientes del Cena: \n ")
    CrearCena.write("-Ingredientes: " + ingredientes_cena + '\n')
    instrucciones_cena = input("-Digita las instrucciones de preparacion: \n")
    CrearCena.write("-Instrucciones: " + instrucciones_cena + '\n')
    print('\n')



#SubMenu para ver los platos de Cena
def cena_ver():
    print("\t     -- CENAS --")
    Folder_name = "FolderCena/"
    Files = os.listdir(Folder_name)
    index = 1
    for f in Files:
        print(index, "-", f)
        index = index + 1

    Seleccion = int(input("-Seleccione el Cena: " + '\n'))
    selected_file = Files[Seleccion - 1]
    x = open("FolderCena/" + selected_file, "r")
    print(x.read())


# Ciclo while para validar las teclas
while True:
    # Mostramos el menu
    menu2()
    # Opciones para el usuario
    opcionMenu2 = input("-Digita la opcion que desea >> ")

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
        input("-No has pulsado ninguna opción correcta...")
