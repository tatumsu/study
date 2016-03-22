<?php
	include_once "classes/Page_Data.class.php";
	$pageData = new Page_Data();
	$pageData->title = "Thomas Blom Hansen: Portfolio site";
	$pageData->content = include_once "views/navigation.php";
	$pageData->externalStyle = "<link href='css/layout.css' rel='stylesheet' />";

	$navigationIsClicked = isset($_GET['page']);
	if ($navigationIsClicked ) {
		$fileToLoad = $_GET['page'];
		$pageData->content .=include_once "views/$fileToLoad.php";
	} else {
		$fileToLoad = "skills";
	}

	$pageData->embeddedStyle = "
	<style>
	nav a[href *= '?page=$fileToLoad']{
	padding:3px;
	background-color:white;
	border-top-left-radius:3px;
	border-top-right-radius:3px;
	}
	</style>";

	$page = include_once "templates/page.php";
	echo $page
?>