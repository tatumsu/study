<?php

include_once "models/Table.class.php";

class Blog_Entry_Table extends Table {
    
    //notice there are two underscore characters in __construct
    public function __construct ( $db ) {
        $this->db = $db;
    }
    
   
    public function saveEntry ( $title, $entry ) {
        //notice placeholders in SQL string. ? is a placeholder
        //notice the order of attributes: first title, next entry_text
        $entrySQL = "INSERT INTO blog_entry ( title, entry_text ) 
                     VALUES ( ?, ?)";
        $entryStatement = $this->db->prepare( $entrySQL );
        //create an array with dynamic data
        //Order is important: $title must come first, $entry second
        $formData = array( $title, $entry ); 
       //changes start here
        //$this is the object's way of saying 'my'
        //so $this->makeStatement calls makeStatement of Blog_Entry_Table
        $entryStatement = $this->makeStatement( $entrySQL, $formData );
        //end of changes
        return $this->db->lastInsertId();

    }
    
    public function getAllEntries () {
        $sql = "SELECT entry_id, title, SUBSTRING(entry_text, 1, 150) AS intro  FROM blog_entry";
        $statement = $this->makeStatement($sql);
        return $statement;
    }

    
    public function getEntry( $id ){
        $sql = "SELECT entry_id, title, entry_text, date_created
                FROM blog_entry
                WHERE entry_id = ?"; 
        $data = array($id);
        //call the new DRY method
        $statement = $this->makeStatement($sql, $data);
        $model = $statement->fetchObject();
        return $model;
    }

    
    //declare a new method inside the Blog_Entry_Table class
    public function deleteEntry ( $id ) {
        $this->deleteCommentsByID( $id );
        $sql = "DELETE FROM blog_entry WHERE entry_id = ?";
        $data = array( $id );
        $statement = $this->makeStatement( $sql, $data );
    }

    public function updateEntry ( $id, $title, $entry) {
        $sql = "UPDATE blog_entry 
                SET title = ?, 
                entry_text = ? 
                WHERE entry_id = ?";
        $data = array( $title, $entry, $id );
        $statement = $this->makeStatement( $sql, $data) ;
        return $statement;
    }
    
    public function searchEntry ( $searchTerm ) {
        $sql = "SELECT entry_id, title FROM blog_entry
                WHERE title LIKE ?
                OR entry_text LIKE ?";
        $data = array( "%$searchTerm%", "%$searchTerm%" );
        $statement = $this->makeStatement($sql, $data);
        return $statement;
    }
    
    private function deleteCommentsByID( $id ) {
        include_once "models/Comment_Table.class.php";
        //create a Comment_Table object
        $comments = new Comment_Table( $this->db );
        //delete any comments before deleting entry
        $comments->deleteByEntryId( $id );
    }







}
