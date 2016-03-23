<?php
//complete code for blog/admin.php
error_reporting( E_ALL );
ini_set( "display_errors", 1 );

include_once "models/Page_Data.class.php";
$pageData = new Page_Data();
$pageData->title = "PHP/MySQL blog demo";
$pageData->addCSS("css/blog.css");
$pageData->addScript("js/editor.js");
//$pageData->content = include_once "views/admin/admin-navigation.php";

$dbInfo = "mysql:host=localhost;dbname=simple_blog";
$dbUser = "root";
$dbPassword = "";
$db = new PDO( $dbInfo, $dbUser, $dbPassword );
$db->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION );

/*
$navigationIsClicked = isset( $_GET['page'] );
if ( $navigationIsClicked ) {
    //prepare to load corresponding controller
    $contrl = $_GET['page'];
} else {
    //prepare to load default controller
    $contrl = "entries";
}
//load the controller
$pageData->content .= include_once "controllers/admin/$contrl.php";
*/

include_once "models/Admin_User.class.php";
$admin = new Admin_User();
//load the login controller, which will show the login form
$pageData->content = include_once "controllers/admin/login.php";

//add a new if statement
//show admin module only if user is logged in
if( $admin->isLoggedIn() ) {
    $pageData->content .= include "views/admin/admin-navigation.php";
    $navigationIsClicked = isset( $_GET['page'] );
    if ($navigationIsClicked ) {
        $controller = $_GET['page'];
    } else {
        $controller = "entries";
    }
    $pathToController = "controllers/admin/$controller.php";    
    $pageData->content .= include_once $pathToController;
} //end if-statement



$page = include_once "views/page.php";
echo $page;

