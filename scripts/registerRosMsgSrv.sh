#!/bin/sh
ROOT_DIR="$(realpath $(dirname ${BASH_SOURCE[0]}))/.."
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$ROOT_DIR
export PYTHONPATH=$PYTHONPATH:$ROOT_DIR/build-native
