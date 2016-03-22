<?php
	//complete code for ch3/test-assoc-array.php
	$boy['name'] = "Thomas";
	$boy['year-of-birth'] = 1972;
	$boy['height'] = "193cm";
	$out = "<pre>";
	$out .=print_r($boy, true);
	$out .= "</pre>";

	echo $out;
?>