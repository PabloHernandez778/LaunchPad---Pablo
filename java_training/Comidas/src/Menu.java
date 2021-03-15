import java.util.Scanner;

public class Menu {
    public Comida ingresarNuevaComida(int tipo){
        System.out.println("Digite comida: ");
        String nombreComida = "";
        String ingredientes = "";
        Scanner entradaEscaner = new Scanner(System.in);
        nombreComida = entradaEscaner.nextLine();
        System.out.println("Digite ingredientes: ");
        ingredientes = entradaEscaner.nextLine();
        return new Comida(nombreComida, ingredientes, tipo);
    }
}
