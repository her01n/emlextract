#!/usr/bin/python3

from argparse import ArgumentParser
from base64 import b64decode
from email.parser import Parser
from re import compile
from os.path import dirname, join, splitext
from os import makedirs

parser = ArgumentParser(description="Extract EML file.")
parser.add_argument("source", metavar="FILE", nargs=1, help="Input file")
parser.add_argument("-f" , "--force", dest="force", action="store_true", help="Overwrite output files")
args = parser.parse_args()

source = args.source[0]
force = args.force
name = splitext(source)[0]
attachments = join(dirname(source), "attachments")

if force:
    mode = "wb"
else:
    mode = "xb"

filename_pattern = compile(r"=\?UTF-8\?B\?(.+)\?=")

with open(source, "r") as input:
    email = Parser().parse(input)

success = False
counter = 1

for part in email.walk():
    disposition = part.get_content_disposition()
    if disposition and disposition.lower() == "attachment":
        makedirs(attachments, exist_ok=True)
        filename = part.get_filename()
        if not filename:
            ext = mimetypes.guess_extension(part.get_content_type()) or ""
            filename = 'attachment%3d%s' % (counter, ext)
            counter += 1
        elif filename_pattern.match(filename):
            decoded = ""
            for match in filename_pattern.finditer(filename):
                decoded += b64decode(match.group(1)).decode("utf-8")
            filename = decoded
        with open(join(attachments, filename), mode) as output:
            output.write(part.get_payload(decode=True))
            success = True
    elif part.get_content_type() == "text/html":
        with open(name + ".html", mode) as output:
            output.write(part.get_payload(decode=True))
            success = True
    elif part.get_content_type() == "text/plain":
        with open(name + ".txt", mode) as output:
            output.write(part.get_payload(decode=True))
            success = True

if not success:
    sys.exit(2)

