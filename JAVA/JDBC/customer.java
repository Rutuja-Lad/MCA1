import java.sql.*;
import java.util.*;

class customer
{
    public static void main(String args[])
    {
        PreparedStatement ps=null;
        Connection con=null;
        try
        {
        con=DriverManager.getConnection("jdbc:mysql://localhost:3306/xyz","root","");
        if(con!=null)
        {
            System.out.println("Connection established");
        }
        Scanner sc=new Scanner(System.in);
        String query="insert into employee values(?,?,?,?)";
        ps=con.prepareStatement(query);

        System.out.println("Customer detail");
        System.out.println("Enter C_id");
        int c_id=sc.nextInt();

        System.out.println("Enter name");
        String c_name=sc.next();

        System.out.println("Enter address");
        String c_add=sc.next();

        System.out.println("Enter phone no");
        int c_phno=sc.nextInt();

        ps.setInt(1,c_id);
        ps.setString(2,c_name);
        ps.setString(3,c_add);
        ps.setInt(4,c_phno);

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