<<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<?php
$x = 5;
$y = 10;

function myTest() {
    global $x, $y;
    $y = $x + $y;
}

myTest();
echo $y; // outputs 15
?>
</body>
</html>