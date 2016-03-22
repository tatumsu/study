<?php
	class Page_Data {
		public $title = "";
		public $content = "";
		public $externalStyle = "";
		public $embeddedStyle = "";
		
		public function addCSS( $href ){
			$this->css .= "<link href='$href' rel='stylesheet' />";
		}
	}
?>