import java.io.*;
import java.net.*;

public class ServeurUDP {
    public static void main(String[] args) {

            // Créer un DatagramSocket sur le port 1234
            DatagramSocket sock = new DatagramSocket(1234);
		String s="Hello World";
		byte [ ] data = s . getBytes ( ) ;

            while (true) {
                // Afficher un message de debug pour indiquer que le serveur attend des données
                System.out.println("- Waiting for data");

                // Créer un DatagramPacket pour recevoir les données (taille de 1024 bytes)
                DatagramPacket packet = new DatagramPacket(new byte[1024], 1024);

                // Attendre la réception des données
                sock.receive(packet);

                // Convertir les données reçues en chaîne de caractères
                String str = new String(packet.getData());

                // Afficher les données reçues
                System.out.println("str = " + str);
            }
}

}
