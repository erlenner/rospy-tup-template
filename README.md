# A template for building ROS nodes in python with tup on ubuntu

This template implements the basic publish and subscribe rosnodes, using a custom message located in ros/msg/.

### How to create a new ROS node repo.

Create a [blank repo](https://github.com/organizations/AscendNTNU/repositories/new), do not initialize the repo with a README or any other files.

Clone this repo bare to your machine using: `git clone --bare git@github.com:AscendNTNU/rospy-tup-template.git`

Go into the repo you just cloned: `cd rospy-tup-template/`

Mirror push to the new repository you just created `git push --mirror git@github.com:AscendNTNU/EMPTY-REPO-NAME.git`

NB! Make shure you are pushing to the correct repo, as this will overwrite any existing data.

Remove the bare clone
```
cd ..
rm -rf rospy-tup-template.git/
```
Delete the example branches from your new repo.

You can now clone this new repo to your machine and start development.

### Prerequisites:
Install [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu).

To install tup, run ["./scripts/getTup.sh""](scripts/getTup.sh).

An unofficial, slightly outdated version of tup is also available as a debian package for ubuntu: [https://launchpad.net/~cezary0/+archive/ubuntu/tup](https://launchpad.net/~cezary0/+archive/ubuntu/tup). However this template is meant to be used with the tup version that getTup.sh downloads and builds so use the debian package at your own risk.

### Building:
To build, run "tup" from the command line.

The building process generates python code for the messages and services in ros/msg and ros/srv and makes a shell script that makes the python message/service code accessible from your python scripts in the source folders by including its path in PYTHONPATH before calling the sources main.py script. This means you only have to run tup after you have changed the ROS message or service files, or after you have changed the directory structure in src/ by creating, deleting or renaming source directories. You don't need to run tup if you have only made changes to the source code (the python scripts in the folders in src/). This includes file creation/deletion/renaming. Just make sure there is a main.cpp file in each source directory that calls all your code.

To automatically build on file change and see building log messages in current shell, run "tup monitor -f -a --autoparse".

### Running
Outputs have the same directory path and name as the source directory, starting from build-native/.
(For example the output shell script from the source directory, src/publisher/ have the path build-native/src/publisher/publisher.)

Run the command "roscore" to run the "ROS Master" that the rosnodes need to register with in order to communicate with each other.

### Editing source
Source files are located in separate directories in src/.
