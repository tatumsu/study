<?php
//complete source code for views/gallery.php
//function call
return showImages();

//function defintion
function showImages()
{
    $out = "<h1>Image Gallery</h1>";
    $out .= "<div id='container'>";
    $folder = "img";

    $filesInFolder = new DirectoryIterator($folder);
    while ($filesInFolder->valid()) {
        $file     = $filesInFolder->current();
        $filename = $file->getFilename();
        $src      = "$folder/$filename";

        $fileInfo = new Finfo(FILEINFO_MIME_TYPE);
        $mimeType = $fileInfo->file($src);
        if ($mimeType === 'image/jpeg') {
            $out .= "<div class='thumb'><img src='$src' /></div>";
        }

        $filesInFolder->next();
    }
    $out .= "</div>";
    return $out;
}
