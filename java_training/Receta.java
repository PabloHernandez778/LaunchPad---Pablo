public class Receta {

	private int calorias;
	private String name;

	public Receta(int contenidoCalorico, String titulo) {
		calorias = contenidoCalorico;
		name = titulo;
	}

	public String obtenerTitulo() {
		return name + " - " + calorias;
	}

	public void cambiarCalorias(int contenidoCalorico) {
		if (contenidoCalorico <= 0)
			return;
		else
			calorias = contenidoCalorico;
	}

}
 
