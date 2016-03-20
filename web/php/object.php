<?php

$user = new stdClass();
$user->name = "tatum.su";
$user->email = "tatum.su@augmentum.com";

$title = "PHP Object";
$content = "<h1>$user->name, your email is: $user->email</h1>";
//indicate the relative path to the file to include
$page = include_once "template.php";
echo $page;

?>