#!/bin/sh
# WARNING: Modifies ~/.bashrc
if [ "$#" -ne 1 ]
then
  echo -e "Usage: ./ignoreAutocompleteForPackageNamePermamently <PACKAGE_NAME>"
else
  echo "export FIGNORE=\$FIGNORE:$1" >> ~/.bashrc
fi
