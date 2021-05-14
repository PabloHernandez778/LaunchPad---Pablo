import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pablo3408",
    database="foodapp"
)

# Menu principal
def menu2():
    os.system('cls')
    print("\t   --MENU PRINCIPAL--     ")
    print("\tSi desea agregar una comida pulse 1")
    print("\t2.Buscar       ")
    print("\t3. Salir")

# SubMenu para insertar nuevos snacks
def food_insetrar():

    print("\t     -- INSERTE COMIDA--   ")
    tipo = input("Digite el tipo de comida: ")
    nombre_comida = input("-Digite el nombre de la comida:  ")
    calo = input("Digite las calorias: ")
    ingredientes = input("-Introduce los ingredientes de la comida: \n ")
    instrucciones = input("-Digita las instrucciones de preparacion: \n")
    print('\n')

    val = (tipo, nombre_comida,calo, ingredientes, instrucciones)
    mycursor = mydb.cursor()
    sqlFormula = "INSERT INTO appfood1 (ID, Tipo, Nombre, Calorias, Ingredientes, Instrucciones) VALUES(UUID(), %s, %s, %s, %s, %s)"
    mycursor.execute(sqlFormula, val)
    mydb.commit()

    print("Comida save")

def food_buscar():
    mycursor = mydb.cursor()
    search = input("Buscar:")
    sql_food = "SELECT Nombre, Calorias, Ingredientes, Instrucciones FROM appfood1 WHERE Nombre = %s "
    val = (search,)
    mycursor.execute(sql_food, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)




# Ciclo while para validar las teclas
while True:
    # Mostramos el menu
    menu2()
    # Opciones para el usuario
    opcionMenu2 = input("-Digita la opcion que desea >> ")

    if opcionMenu2 == "1":
        food_insetrar()
    elif opcionMenu2 == "2":
        food_buscar()
    elif opcionMenu2 =="3":
        break
    else:
        print("")
        input("-No has pulsado ninguna opción correcta...")