<?php
class Page_Data
{
    public $title         = "";
    public $content       = "";
    public $externalStyle = "";
    public $embeddedStyle = "";

    public $scriptElements = "";
    //declare a new method for adding Javascript files
    public function addScript($src)
    {
        $this->scriptElements .= "<script src='$src'></script>";
    }

    public function addCSS($href)
    {
        $this->css .= "<link href='$href' rel='stylesheet' />";
    }
}
