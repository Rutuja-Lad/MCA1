//Prepate Statement
import java.sql.*;  
class man
{  
    public static void main(String args[])
    {  
    try
    {  
        //Class.forName("oracle.jdbc.driver.OracleDriver");  
  
        Connection con=DriverManager.getConnection( "jdbc:mysql://localhost:3306/man","root","");  
  
        PreparedStatement stmt=con.prepareStatement("insert into man values(?,?,?)");  
        stmt.setInt(1,101);//1 specifies the first parameter in the query  
        //stmt.setInt(1,101);//1 specifies the first parameter in the query  
        stmt.setString(1,"Ratan");
        stmt.setString(1,"Professor");


        stmt.setInt(2,102);//1 specifies the first parameter in the query  
        //stmt.setInt(1,101);//1 specifies the first parameter in the query  
        stmt.setString(2,"Prem");
        stmt.setString(2,"Banker");
        
        stmt.setInt(1,101);//1 specifies the first parameter in the query  
        //stmt.setInt(1,101);//1 specifies the first parameter in the query  
        stmt.setString(1,"Ratan");
        stmt.setString(1,"Professor");
  
        int i=stmt.executeUpdate();  
        System.out.println(i+" records inserted");  
  
        con.close();  
  
    }
    catch(Exception e)
    { 
        System.out.println(e);
    
    }
    }
  
}  
