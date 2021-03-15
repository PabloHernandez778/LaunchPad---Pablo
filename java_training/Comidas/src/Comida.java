public class Comida {
    String nombre;
    String ingredientes;
    int tipo;

    public Comida(String n, String i, int t) {
        nombre = n;
        ingredientes = i;
        tipo = t;

    }

    String getNombre() {
        return nombre;
    }

    String getIngredientes() {
        return ingredientes;
    }

    void setNombre(String n) {
        nombre = n;
    }

    void setIngredientes(String i) {
        ingredientes = i;
    }

    int getTipo() {
        return tipo;
    }

    void setTipo(int t) {
        tipo = t;
    }

    String printTipo() {
        if (tipo == 1)
            return "Snack";
        if (tipo == 2)
            return "Desayuno";
        if (tipo == 3)
            return "Almuerzo";
        if (tipo == 4)
            return "Cena";
        if (tipo == 5)
            return "Postre";
        else
            return "Unknown";

    }
}
