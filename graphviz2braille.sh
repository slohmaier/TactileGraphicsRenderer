#!/bin/sh
if [ "$1" = "-h" ]; then
    echo "$0 [INPUT FOT] [OUTPUT SVG]"
    exit 0
fi

if [ ! -e "$1" ] || [ "x$2" = "x" ]; then
    echo "Error: Try \$0 -h."
    exit 1
fi

dot -Tpng "-Nfontname=Braille29 DE" -Nfontsize=29 \
    "-Efontname=Braille29 DE" -Efontsize=29 \
    $1 > $2
