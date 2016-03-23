<?php
class Uploader {
    private $filename;
    private $fileData;
    private $destination;
    private $errorMessage;
    //new code: add a property for standard PHP error codes
    private $errorCode;

    //declare a constructor method
    public function __construct( $key ) {
        $this->filename = $_FILES[$key]['name'];
        $this->fileData = $_FILES[$key]['tmp_name'];
        $this->errorCode = ( $_FILES[$key]['error'] );
    }
    
    public function saveIn( $folder ) {
        $this->destination = $folder;
    }
    
    public function save () {
    //call the new method to look for upload errors
    //if it returns TRUE, save the uploaded file
    if ( $this->readyToUpload() ) {
        move_uploaded_file( 
             $this->fileData, 
            "$this->destination/$this->filename" );
    } else {
        //if not create an exception - pass error message as argument
        $exc = new Exception( $this->errorMessage );
        //throw the exception
        throw $exc;
    }
}

    
    private function readyToUpload(){
        $folderIsWriteAble = is_writable( $this->destination );
        if( $folderIsWriteAble === false ){ 
            //provide a meaningful error message
            $this->errorMessage = "Error: destination folder is ";
            $this->errorMessage .= "not writeable, change permissions";
            //indicate that code is NOT ready to upload file
            $canUpload = false;
        } else if ( $this->errorCode === 1 ) {
            $maxSize = ini_get( 'upload_max_filesize' );
            $this->errorMessage = "Error: File is too big. ";
            $this->errorMessage .= "Max file size is $maxSize";
            $canUpload  = false;
        } else if ( $this->errorCode > 1 ) {
            $this->errorMessage = "Something went wrong! ";
            $this->errorMessage .= "Error code: $this->errorCode";
            $canUpload = false;
        } else {
            //assume no other errors - indicate we're ready to upload
            $canUpload = true;
        }
        return $canUpload ;
    }


}
