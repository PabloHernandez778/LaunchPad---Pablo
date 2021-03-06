import java.util.Scanner; //Importación del código de la clase Scanner desde la biblioteca Java

public class crearComida {
    public static void main(String[]args){
        System.out.println("Digite comida");
        String entradaTeclado = "";
        String ingredientes = "";
        Scanner entradaEscaner = new Scanner(System.in);
        entradaTeclado = entradaEscaner.nextLine();
        ingredientes = entradaEscaner.nextLine();
        System.out.println("Entrada por teclado es:\""+ entradaTeclado+"\"" + ingredientes + "\"");

    }
}
