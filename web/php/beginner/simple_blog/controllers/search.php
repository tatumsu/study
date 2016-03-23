<?php
//complete code for controllers/search.php
include_once "models/Blog_Entry_Table.class.php";
$blogTable = new Blog_Entry_Table( $db );

$searchOutput = "";
if ( isset($_POST['search-term']) ){
    $searchTerm = $_POST['search-term'];
    $searchData = $blogTable->searchEntry( $searchTerm ) ;
    $searchOutput = include_once "views/search-results-html.php"; 
}
//delete all the code your wrote for testing the searchEntry method
return $searchOutput;
