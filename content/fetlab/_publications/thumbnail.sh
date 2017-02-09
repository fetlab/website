#!/usr/local/bin/bash
convert -thumbnail x200 -background white -alpha remove "$1[0]" "$2"
