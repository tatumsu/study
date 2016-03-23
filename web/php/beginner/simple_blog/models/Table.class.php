<?php
//complete code for models/Table.class.php

class Table {
    //notice protected, not private
    protected $db;
    
    public function __construct ( $db ) {
        $this->db = $db;
    }

    //notice protected, not private    
    protected function makeStatement ( $sql, $data = null ){
        $statement = $this->db->prepare( $sql );
        try {
            $statement->execute( $data );
        } catch (Exception $e) {
            $exceptionMessage = "<p>You tried to run this sql: $sql <p>
                    <p>Exception: $e</p>";
            trigger_error($exceptionMessage);
        }        
        return $statement;
    } 
}
