import java.sql.*;
import java.util.Scanner;

class Emp {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    Connection con = null;
    PreparedStatement pstmt = null;
    Statement st = null;
    ResultSet rs = null;
    try {
        // Class.forName("com.mysql.cj.jdbc.Driver");
      con =
        DriverManager.getConnection(
          "jdbc:mysql://localhost:3306/mca",
          "root",
          ""
        );
      if (con != null) {
        System.out.println("yrs");
      }else{
        System.out.println("Failed");
      }
        /*int ch;
        do {
          System.out.println(
            "\n1.View \n2.Insert \n3.Update \n4.Delete \n5.Exit"
          );
          System.out.println("Enter your choice: ");
          ch = sc.nextInt();
          switch (ch) {
            case 1:
              st = con.createStatement();
              rs = st.executeQuery("select * from emp");
              System.out.println(
                "Sno" + "\t" + "Sname" + "\t" + "Dept" + "\t" + "Sal"
              );
              System.out.println("--------------------------------");
              while (rs.next()) {
                System.out.println(
                  rs.getInt("sno") +
                  "\t" +
                  rs.getString("ename") +
                  "\t" +
                  rs.getString("dept") +
                  "\t" +
                  rs.getInt("sal")
                );
              }
              break;
            case 2:
              pstmt = con.prepareStatement("insert into emp values(?,?,?,?)");

              System.out.println("\nEnter E_Number:");
              int sno = sc.nextInt();
              pstmt.setInt(1, sno);

              sc.nextLine();
              System.out.println("Enter Name:");
              String name = sc.nextLine();
              pstmt.setString(2, name);

              System.out.println("Enter Department:");
              String dept = sc.nextLine();
              pstmt.setString(3, dept);

              System.out.println("Enter Salary:");
              int sal = sc.nextInt();
              pstmt.setInt(4, sal);

              int result = pstmt.executeUpdate();
              System.out.println(result + " Record Inserted\n");
              break;
            case 3:
              String SQL2 = "update emp set sal = ? where sno=?";
              pstmt = con.prepareStatement(SQL2);

              System.out.println("Enter Eon which has to be Update: ");
              int sn = sc.nextInt();

              System.out.println("Enter Salary for update:");
              int salary = sc.nextInt();

              pstmt.setInt(2, sn);
              pstmt.setFloat(1, salary);

              int result2 = pstmt.executeUpdate();
              System.out.println(result2 + " Record Updated\n");
              break;
            case 4:
              String SQL3 = "delete from emp where sno =?";
              pstmt = con.prepareStatement(SQL3);
              System.out.println("\nEnter Eno whose record you want delete ");
              int s_no = sc.nextInt();
              pstmt.setInt(1, s_no);
              int result3 = pstmt.executeUpdate();
              System.out.println(result3 + " Record Deleted\n");
              break;
          }
        } while (ch < 5);
      }*/
      con.close();
      st.close();
      rs.close();
      sc.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}