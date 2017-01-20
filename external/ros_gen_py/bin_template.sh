#!/bin/bash
DIR=$(dirname $(realpath "$0"))
PYTHONPATH=$PYTHONPATH:`find $DIR -type d -printf ":%p"` python $DIR/../../../src/$(basename "$0")/$(basename "$0").py "$@"
