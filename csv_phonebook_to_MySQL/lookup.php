<?php
$con= new mysqli("localhost","test","111111","testing");

$NUMBER = $_GET['NUMBER'];
//$NUMBER = '111111111111';

// Check connection
if (mysqli_connect_errno())
      {
      echo "Failed to connect to MySQL: " . mysqli_connect_error();
      }

$result = mysqli_query($con, "SELECT name FROM phonebook
    WHERE phone LIKE '%{$NUMBER}%'");

if ($result->num_rows > 0) {
while ($row = mysqli_fetch_array($result))
{
//echo $row['name'] . " " . $row['number'];
$NAME = $row['nome'];
echo $NAME;
}
} else {
echo $NUMBER;
}
mysqli_close($con);

?>
