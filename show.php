<?php
echo "##########   Data retrive from MYSQL Database############ </br>";
echo " filename ### file_size #### time ########## </br>";
echo "**************************************************</br>";
//echo "\n";
   $dbhost = 'localhost';
   $dbuser = 'admin';
   $dbpass = 'admin123';
   $dbname ='Backup';
   $conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
   //echo  "---connection mysql----"; 

   //if(! $conn->connect_error ) {
	//   die('Could not connect: ' . $conn->connect_error);
	// }
	
   $sql="select * from backup";
   $result = $conn ->query($sql);
	

   if ($result->num_rows > 0) {
	       // output data of each row
	       while($row = $result->fetch_assoc()) {
		       echo "id:".$row["id"]."  &nbsp;&nbsp;    "."file_name: ". $row["file_name"]."  &nbsp;&nbsp;      "."file_size:".$row["file_size"]."   &nbsp;&nbsp;       "."time:".$row["mtime"]."</br>" ;
		       //echo "\n";
	                    }
	                    } else {
	                        echo "0 results";
	                        }
	                        $conn->close();



?>
