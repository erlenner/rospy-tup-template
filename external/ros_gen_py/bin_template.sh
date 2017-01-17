#!/bin/bash
DIR=$(dirname $(realpath "$0"))
PYTHONPATH="$PYTHONPATH:$DIR" python $DIR/../../../src/$(basename "$0")/$(basename "$0").py "$@"
