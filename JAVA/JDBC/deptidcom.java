public import java.sql.*;
class Emp
{
public static void main(String args[])
{
Connection con=null;
try
{
con=DriverManager.getConnection("jdbc:mysql://localhost:3306/javadb","root","admin");
if(con!=null)
{
System.out.println("Connection Established");
}
Statement st=con.createStatement();
ResultSet rs=st.executeQuery("select * from emp where edept='comp'");
while(rs.next())
{
System.out.println(rs.getInt(1)+""+rs.getString(2)+""+rs.getInt(3)+" +rs.getString(4));
}
rs.close();
}
catch(Exception e){}
}
}
 
