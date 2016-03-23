<?php
//complete code for controllers/admin/editor.php
include_once "models/Blog_Entry_Table.class.php";
$entryTable = new Blog_Entry_Table( $db );

$editorSubmitted = isset( $_POST['action'] );
if ( $editorSubmitted ) {
    $buttonClicked = $_POST['action'];
    $save = ( $buttonClicked === 'save' );
    $id = $_POST['id'];
    $insertNewEntry  = ( $save and $id === '0' );
    $deleteEntry = ($buttonClicked === 'delete');
    $updateEntry = ( $save and $insertNewEntry === false );    
    $title = $_POST['title'];
    $entry = $_POST['entry'];

    if ( $insertNewEntry ) {

        $savedEntryId = $entryTable->saveEntry( $title, $entry );
    } else if ( $updateEntry ){
        $entryTable->updateEntry( $id, $title, $entry );
    
        $savedEntryId = $id;
    } else if ( $deleteEntry ) {
        $entryTable->deleteEntry( $id );
    }


}

$entryRequested = isset( $_GET['id'] );
if ( $entryRequested ) {
    $id = $_GET['id'];
    $entryData = $entryTable->getEntry( $id );
    $entryData->entry_id = $id;
    //new code: show no message when entry is loaded initially
    $entryData->message = "";
}

//new code below: an entry was saved or updated
$entrySaved = isset( $savedEntryId );
if ( $entrySaved ) {
    $entryData = $entryTable->getEntry( $savedEntryId );
    //display a confirmation message
    $entryData->message = "Entry was saved";
}


$editorOutput = include_once "views/admin/editor-html.php";
return $editorOutput;




