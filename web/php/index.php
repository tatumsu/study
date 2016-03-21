<?php
	$pageData = new stdClass();

	$pageData->title = "Thomas Blom Hansen: Portfolio site";
	$pageData->content = include_once "views/navigation.php";

	$navigationIsClicked = isset($_GET['page']);
	if ($navigationIsClicked ) {
		$fileToLoad = $_GET['page'];
		$pageData->content .=include_once "views/$fileToLoad.php";
	}

	$page = include_once "templates/page.php";
	echo $page
?>