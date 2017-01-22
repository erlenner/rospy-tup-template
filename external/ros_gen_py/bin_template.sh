#!/bin/bash
DIR=$(dirname $(realpath "$0"))
PYTHONPATH=$PYTHONPATH:`find $DIR -type d -printf ":%p"` python $DIR/../../../src/$(basename "$DIR")/main.py "$@"
