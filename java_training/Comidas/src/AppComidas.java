import java.util.Scanner;

public class AppComidas {

    public static void main(String[] args) {
        // write your code here
        Scanner sn = new Scanner(System.in);
        boolean salir = false;
        int opcion;

        while (!salir) {
            System.out.println("     -MENU DE COMIDAS-    ");
            System.out.println("1- Snack");
            System.out.println("2- Desayuno");
            System.out.println("3- Almuerzo");
            System.out.println("4- Cena");
            System.out.println("5- Postre");
            System.out.println("6- Salir");

            System.out.println("Escribe una de las opciones: ");
            opcion = sn.nextInt();
            Menu menu = new Menu();

            switch (opcion) {
                case 1:
                    System.out.println("Has seleccionado la opcion 1");
                    Comida snack = menu.ingresarNuevaComida(1);
                    new Impresor().imprimir(snack);
                    break;
                case 2:
                    System.out.println("Has seleccionado la opcion 2");
                    Comida desayuno = menu.ingresarNuevaComida(2);
                    new Impresor().imprimir(desayuno);
                    break;
                case 3:
                    System.out.println("Has Seleccionado la opcion 3");
                    Comida almuerzo = menu.ingresarNuevaComida(3);
                    new Impresor().imprimir(almuerzo);
                    break;
                case 4:
                    System.out.println("Has seleccionado la opcion 4");
                    Comida cena = menu.ingresarNuevaComida(4);
                    new Impresor().imprimir(cena);
                    break;
                case 5:
                    System.out.println("Has seleccionado la opcion 5");
                    Comida postre = menu.ingresarNuevaComida(5);
                    new Impresor().imprimir(postre);
                    break;
                case 6:
                    salir = true;
                    break;
                default:
                    System.out.println("Solo numeros entre 1 y 5");
            }
        }
    }


    }
