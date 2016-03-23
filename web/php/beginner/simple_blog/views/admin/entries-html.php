<?php
//complete code for views/admin/entries-html.php
if( isset( $allEntries ) === false ) {
    trigger_error('views/admin/entries-html.php needs $allEntries');
}

$entriesAsHTML = "<ul>";
while ( $entry = $allEntries->fetchObject() ) {
    //notice two URL variables are encoded in the href
    $href = "admin.php?page=editor&amp;id=$entry->entry_id";
    $entriesAsHTML .= "<li><a href='$href'>$entry->title</a></li>";
}

$entriesAsHTML .= "</ul>";
return $entriesAsHTML;
