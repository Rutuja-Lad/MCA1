    //Write a JDBC program to display the details of employees (eno, ename,
    import java.sql.*;
    class emp4
    {
        public static void main(String args[])
        {
            Connection con=null;
            try
            {
                con=DriverManager.getConnection("jdbc:mysql://localhost:3306/emp","root","");
                if(con!=null)
                {
                System.out.println("Connection Established");
                }
                Statement st=con.createStatement();
                ResultSet rs=st.executeQuery("select * from emp where emp_dept='IT'");
                while(rs.next())
                {
                System.out.println(rs.getInt(1)+""+rs.getString(2)+""+rs.getString(3));
                }
                rs.close();
            }
            catch(Exception e){}
        }
     }

