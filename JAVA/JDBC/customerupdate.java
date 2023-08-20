import java.sql.*;
import java.util.*;

class customerupdate
{
    public static void main(String args[])
    {
        PreparedStatement ps=null;
        Connection con=null;
        try
        {
        con=DriverManager.getConnection("jdbc:mysql://localhost:3306/customer","root","");
        if(con!=null)
        {
            System.out.println("Connection established");
        }
        Scanner sc=new Scanner(System.in);
        String query="update customer_info set c_add='thane' where c_add='pune'";
        ps=con.prepareStatement(query);

        
       

        int no=ps.executeUpdate();
        if(no!=0)
        System.out.println("Data inserted successfully");
        else
        System.out.println("Data is not inserted ");
        con.close();
    }
    catch(Exception e)
    {
        e.printStackTrace();
    }
 }
}
