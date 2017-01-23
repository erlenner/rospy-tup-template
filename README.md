# A template for building ROS nodes in python with tup on ubuntu

This template implements the basic publish and subscribe rosnodes, using a custom message located in ros/msg/.

### Prerequisites:
Install [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu).

To install tup, run ["./scripts/getTup.sh""](scripts/getTup.sh).

An unofficial, slightly outdated version of tup is also available as a debian package for ubuntu: [https://launchpad.net/~cezary0/+archive/ubuntu/tup](https://launchpad.net/~cezary0/+archive/ubuntu/tup). However this template is meant to be used with the tup version that getTup.sh downloads and builds so use the debian package at your own risk.

### Building:
To build, run "tup" from the command line.

The building process generates python code for the messages and services in ros/msg and ros/srv and makes a shell script that makes the python message/service code accessible from your python scripts in the source folders by including its path in PYTHONPATH before calling the sources main.py script. This means you only have to run tup after you have changed the ROS message or service files, or after you have changed the directory structure in src/ by creating, deleting or renaming source directories. You don't need to run tup if you have only made changes to the source code (the python scripts in the folders in src/). This includes file creation/deletion/renaming. Just make sure there is a main.cpp file in each source directory that calls all your code.

### Running
Outputs have the same directory path and name as the source directory, starting from build-native/.
(For example the output binary from the source directory, src/publisher/ have the path build-native/src/publisher/publisher.)

Run the command "roscore" to run the "ROS Master" that the rosnodes need to register with in order to communicate with each other.

### Editing source
Source files are located in separate directories in src/.