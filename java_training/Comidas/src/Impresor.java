public class Impresor {

    void imprimir(Comida comida) {
        System.out.println("========================");
        System.out.println("Tipo: " + comida.printTipo());
        System.out.println("Nombre: " + comida.getNombre());
        System.out.println("Ingredientes: " + comida.getIngredientes());
    }
}
