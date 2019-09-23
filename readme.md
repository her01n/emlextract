# NAME

emlextract - Extracts message body and attachments from *eml* file

# SYNOPSIS

**emlextract** \[*\--force*\] *FILE*

# DESCRIPTION

If the source file *message.eml* contains a message in plain text format, extracts it to *message.txt*. file.
Likewise if the file contains a message in html format, extracts it to *message.html* file.
The html file is not complete, it does not include *html* or *body* tags.
Both files are written in UTF-8 encoding, transcoding if necessary.
If the source file contains any attachments, they are extracted to *attachments* directory.
This directory is created if missing. 

**-f**, **\--force** 

:   If any file that should be written already exists, the command fails, 
    unless this option is specified. 

# EXIT STATUS

0

:   Ok, at least one file is created.

1

:   EML parsing, read/write error, or output file already exists.

2

:   The source file was parsed without errors, but no message body in a recognized format is found.

