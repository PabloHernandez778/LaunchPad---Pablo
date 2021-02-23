public class HolaMundo {

	public static void main(String[] args) {
		System.out.println("Hola Mundo" );
		//System.out.println("Argumento 1: " + args[0] );

		Receta recetaPrincipal = new Receta(120, "Gallo Pinto");
		recetaPrincipal.cambiarCalorias(100);
		recetaPrincipal.cambiarCalorias(-300);
		System.out.println(recetaPrincipal.obtenerTitulo());
	}
}




