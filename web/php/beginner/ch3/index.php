<?php
	//code listing for index.php
	include_once "classes/Page_Data.class.php";

	$pageData = new Page_Data();
	$pageData->title = "Building and processing HTML forms with PHP";
	$pageData->content = include_once "views/navigation.php";

	//$pageData->content .= "<div>...and a form here</div>";
	$navigationIsClicked = isset($_GET['page']);
	if ( $navigationIsClicked ) {
		$fileToLoad = $_GET['page'];
	} else {
		$fileToLoad = "search";
	}
	$pageData->content .=include_once "views/$fileToLoad.php";

	$page = include_once "templates/page.php";
	echo $page;
?>