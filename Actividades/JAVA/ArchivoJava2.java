import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class ArchivoJava2 {
   public static void main(String[] args) {
      
      String ruta = "C:\\Users\\ema_c\\OneDrive\\Escritorio\\Programacion\\programacion2\\Actividades\\JAVA\\CreandoArchivos\\DatosAlumnos.txt";
      Scanner sc = new Scanner(System.in);
      String nombre = "nombre";
      File archivo = new File(ruta);
      
      try {
        FileWriter indata = new FileWriter(archivo,true);
         
        indata.append("Datos de los Estudiantes de Programacion 2");

        while (!"Salir".equals(nombre)){
        
            System.out.println("Ingrese el nombre del estudiante, sino escriba 'Salir'");
            nombre = sc.next();
            indata.append(nombre);

        }
        indata.close();
        System.out.println("El archivo se ha creado exitosamente.");
      } catch (IOException e) {
         e.printStackTrace();
      }
   }
}






