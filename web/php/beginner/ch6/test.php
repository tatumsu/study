<?php
class Greeter {
    private $greeting = "Hello";
    private $subject = "World";
    
    public function __construct( $g ) {
        $this->greeting = $g;
    }

    public function greet(){
        return "$this->greeting $this->subject";
    }
    
}
$greeter = new Greeter( "Good Morning" );
echo $greeter->greet();
