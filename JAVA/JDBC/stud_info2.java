import java.sql.*;

class stud_info2
{
    public static void main(String args[])
    {
        Connection con;
        try
        {
            con=DriverManager.getConnection("jdbc:mysql://localhost:3306/mca","root","");

            Statement st=con.createStatement();
            ResultSet rs=st.executeQuery("select * from emp where name = 'abc' ");
            while(rs.next())
            {
                System.out.println(rs.getInt(1)+" "+rs.getString(2));
            } 
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
}