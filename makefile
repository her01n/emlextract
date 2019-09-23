default: emlextract.1.gz

emlextract.1: readme.md
	pandoc -s $< -t man -o $@ -V title:EMLEXTRACT -V section:1 -V date:2019-09-23 \
               -V footer:"emlextract 0.1"

emlextract.1.gz: emlextract.1
	gzip <$< >$@

PREFIX ?= /usr/local

install: emlextract.1.gz emlextract.py
	install -D emlextract.py $(PREFIX)/bin/emlextract
	install -D emlextract.1.gz $(PREFIX)/share/man/man1/emlextract.1.gz

