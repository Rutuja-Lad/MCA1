<html>
<head>
<title>PHP MySQL connection example</title>
</head>
<body>
<form method="post">
Enter Student Name : <input type="text" name="n"><br/>
Enter Student Hobby : <input type="text" name="h"><br/>
<input type="submit" value="Update" name="Submit1"> <br/>
</form>
</html>

<?php
$host = "localhost";
$dbusername = "root";
$dbpass = "";
$dbname = "fy";

if(isset($_POST['Submit1']))
{ 
    $n=$_POST['n'];
    $h=$_POST['h'];

    
$con= new mysqli($host, $dbusername, $dbpass, $dbname);
$sql = "update stud set hobby='$h' where sname='$n'";

if(mysqli_query($con,$sql))
{
    echo "record updated";   
}

$query = "select * from stud where sname='$n'"; //Executing the multi query 
$res = mysqli_query($con, $query); //Retrieving the recordsaq
echo "<table border=1>";
      echo "<tr>";
       echo "<th>Sname</th>";
       echo "<th>email</th>";
       echo "<th>phonenumber</th>";
       echo "<th>hobby</th>";
       if($row=mysqli_fetch_array($res))
       {   
           echo "</tr>";
           echo "<tr>";
           echo "<td>$row[0]</td>";
           echo "<td>$row[1]</td>";
           echo "<td>$row[2]</td>";
           echo "<td>$row[3]</td>";
           echo "</tr>";       
       }   
       echo "</table>";   

mysqli_close($con); //Closing the connection
}
?>
