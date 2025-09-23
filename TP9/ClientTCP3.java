import java.io.*;
import java.net.*;

public class ClientTCP3 {
	public static void main(String[] args)  throws Exception
{
	Socket socket = new Socket ("localhost" , 2016);
	DataOutputStream dOut = new DataOutputStream(socket.getOutputStream() );
	dOut .writeUTF("message test");
	Out . writeUTF ( args [0] ) ;
	String rev = new StringBuilder ( msg ) . reverse ( ) . toString ( ) ;
	socket.close();

	}
}
