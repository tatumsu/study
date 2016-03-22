<?php
	//add a new variable and an if statement
	$quizIsSubmitted = isset( $_POST['quiz-submitted'] );
	if ( $quizIsSubmitted ){
		$answer = $_POST['answer'];
		$output = showQuizResponse( $answer );
	} else {
		$output = include_once "views/quiz-form.php";
	}
	//inspect the $_POST superglobal array
	$output .= "<pre>";
	$output .= print_r($_POST, true);
	$output .= "</pre>";

	//keep the return statement as it was
	return $output;

	//declare a new function
	function showQuizResponse( $answer ){
		//changes begin here
		$response = "<p>You clicked $answer";
		if ( $answer === "yes" ){
			$response .= " - I know exactly how you feel!";
		}
		
		$response .= "</p>";
		//end of changes
		$response .= "<p>
		<a href='index.php?page=quiz'>Try quiz again?</a>
		</p>";
		return $response;
	}
?>