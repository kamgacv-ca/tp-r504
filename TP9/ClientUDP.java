import java.io.*;
import java.net.*;

public class ClientUDP
{
    public static void main(String[] args) throws Exception
	{
        String s = "Hello World";
        byte[] data = s.getBytes();
        // Obtenir l'adresse locale (ce code peut lancer une exception)
        InetAddress addr = InetAddress.getLocalHost();
        System.out.println("adresse=" + addr.getHostName());
        // Créer un paquet avec les données à envoyer au serveur
        DatagramPacket packet = new DatagramPacket(data, data.length, addr, 1234);
        // Créer un socket UDP pour envoyer le paquet
        DatagramSocket sock = new DatagramSocket();
        sock.send(packet);
        // Fermer le socket après l'envoi
        sock.receive(packet);
        System.out.println("reception=" + addr.getHostName());
        sock.close();
    }
}
