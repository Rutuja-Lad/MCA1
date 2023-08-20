import java.sql.*;
public class connection
{
    public static void main(String args[])
    {
        Connection con;
        try
        {
            con=DriverManager.getConnection("jdbc:mysql://localhost:3306/dyp","root","");
            if(con!=null)
            {
                System.out.println("done");
            }
            else
            {
                System.out.println("Not done");
            }
        }
        catch(Exception e)
        {
            System.out.println(e); 
        }
    }
}