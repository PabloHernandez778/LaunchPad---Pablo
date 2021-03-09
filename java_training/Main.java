package com.company;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner sn = new Scanner(System.in);
        boolean salir = false;
        int opcion;

        while (!salir){
            System.out.println("     -MENU DE COMIDAS-    ");
            System.out.println("1- Snack");
            System.out.println("2- Desayuno");
            System.out.println("3- Almuerzo");
            System.out.println("4- Cena");
            System.out.println("5- Salir");

            System.out.println("Escribe una de las opciones: ");
            opcion = sn.nextInt();

            switch (opcion){
                case 1:
                    System.out.println("Has seleccionado la opcion 1");
                    Comidas();
                    break;
                case 2:
                    System.out.println("Has seleccionado la opcion 2");
                    break;
                case 3:
                    System.out.println("Has Seleccionado la opcion 3");
                    break;
                case 4:
                    System.out.println("Has seleccionado la opcion 4");
                    break;
                case 5:
                    salir = true;
                    break;
                default:
                    System.out.println("Solo numeros entre 1 y 5");
            }
        }



    }

    public static void Comidas(){
        System.out.println("Digite comida: ");
        String entradaTeclado = "";
        String ingredientes = "";
        Scanner entradaEscaner = new Scanner(System.in);
        entradaTeclado = entradaEscaner.nextLine();
        System.out.println("Digite ingredientes: ");
        ingredientes = entradaEscaner.nextLine();
        System.out.println("La comida es es:\""+ entradaTeclado+"\"" + ingredientes + "\"");
    }
}
