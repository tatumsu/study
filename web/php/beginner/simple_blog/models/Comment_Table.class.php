<?php
//complete code for models/Comment_Table.class.php

//include parent class definition
include_once "models/Table.class.php";

//extend current class from parent class
class Comment_Table extends Table{
    
    //declare a new method inside the Comment_Table class
    public function saveComment ( $entryId, $author, $txt ) {
        $sql = "INSERT INTO comment ( entry_id, author, txt) 
                VALUES (?, ?, ?)";
        $data = array( $entryId, $author, $txt );
        $statement = $this->makeStatement($sql, $data);
        return $statement;
    }
    
    //declare new method inside the Comment_Table class
    public function getAllById ( $id ) {
        $sql = "SELECT author, txt, date FROM comment
                WHERE entry_id = ?
                ORDER BY comment_id DESC";
        $data = array($id);
        $statement = $this->makeStatement($sql, $data);
        return $statement;
    }

    public function deleteByEntryId( $id ) {
        $sql = "DELETE FROM comment WHERE entry_id = ?";
        $data = array( $id );
        $statement = $this->makeStatement( $sql, $data );  
    }


}
