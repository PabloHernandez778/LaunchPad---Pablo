public class Postre extends Comida {
    int calorias;


    public Postre(String n, String i, int t1, int t) {
        super(n, i, t);
    }

    int getCalorias() {
        return calorias;
    }

    void setCalorias(int c) {
        calorias = c;
    }
}
