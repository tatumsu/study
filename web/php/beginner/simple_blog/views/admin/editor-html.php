<?php
//complete code for views/admin/editor-html.php

//new code added here
//check if required data is available
$entryDataFound = isset( $entryData );
if( $entryDataFound === false ){
    //default values for an empty editor
    $entryData = new StdClass();
    $entryData->entry_id = 0;
    $entryData->title = "";
    $entryData->entry_text = "";
    $entryData->message = "";
}

//changes in existing code below
//notice object properties used in <input> and <textarea>
return "
<form method='post' action='admin.php?page=editor' id='editor'>
    <input type='hidden' name='id' value='$entryData->entry_id' />
    <fieldset>
        <legend>New Entry Submission</legend>
        <label>Title</label>    
        <input type='text' name='title' maxlength='150'
        value='$entryData->title' required/>
        <p id='title-warning'></p>
        <label>Entry</label>
        <textarea name='entry'>$entryData->entry_text</textarea>    
        <fieldset id='editor-buttons'>
            <input type='submit' name='action' value='save' />
            <input type='submit' name='action' value='delete' />
            <p id='editor-message'>$entryData->message</p>
        </fieldset>
    </fieldset>
</form>
<script type='text/javascript' src='js/tinymce/tinymce.min.js'> </script>
<script type='text/javascript'>
tinymce.init({
    selector: 'textarea',
    plugins: 'image',
    setup: function (editor) {
        editor.on ('change', function (e) {
            updateEditorMessage();
        });
    }

 });
</script>";

