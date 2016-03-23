<?php
//complete code for controllers/admin/users.php
include_once "models/Admin_Table.class.php";

//is form submitted?
$createNewAdmin = isset( $_POST['new-admin'] );
//if it is...
if( $createNewAdmin ) {
    //grab form input
    $newEmail = $_POST['email'];
    $newPassword = $_POST['password'];    
    $adminTable = new Admin_Table($db);
    try {
        //try to create a new admin user
        $adminTable->create( $newEmail, $newPassword );
        //tell user how it went
        $adminFormMessage = "New user created for $newEmail!";
    } catch ( Exception $e ) {
        //if operation failed, tell user what went wrong
        $adminFormMessage = $e->getMessage();
    }
}
//end of new code


$newAdminForm = include_once "views/admin/new-admin-form-html.php";
return $newAdminForm;
