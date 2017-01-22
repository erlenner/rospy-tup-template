#!/bin/sh
# NEEDS TO BE SOURCED TO WORK
if [ "$#" -ne 1 ]
then
  echo -e "Usage: . ./ignoreAutocompleteForPackageName <PACKAGE_NAME>\nOR\nsource ignoreAutocompleteForPackageName <PACKAGE_NAME>"
else
  export FIGNORE=$FIGNORE:$1
fi
