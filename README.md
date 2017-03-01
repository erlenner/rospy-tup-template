# A template for building ROS nodes in python with tup on ubuntu

This template implements the basic publish and subscribe rosnodes, using a custom message located in ros/msg/.

### Prerequisites:
Install [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu).

To install tup, run `scripts/getTup.sh`.

### Build:
To build, run `tup`.

The building process generates python code for the messages and services in ros/msg and ros/srv and makes a shell script that makes the python message/service code accessible from your python scripts in the source folders by including its path in PYTHONPATH before calling the sources main.py script. This means you only have to run tup after you have changed the ROS message or service files, or after you have changed the directory structure in src/ by creating, deleting or renaming source directories. You don't need to run tup if you have only made changes to the source code (the python scripts in the folders in src/). This includes file creation/deletion/renaming. Just make sure there is a main.py file in each source directory that calls all your code.

To clean all, run `./scripts/clean.sh`. This is mostly needed when debugging the building process.

To see the commands that tup executes, run `tup --verbose`. This is alse mostly needed when debugging the building process.

### Run:
Outputs have the same directory path and name as the source directory, starting from build-native/.
(For example the output script from the source directory, src/publisher/ have the path build-native/src/publisher/publisher.)

Run `roscore` to start the server that the rosnodes uses to communicate with each other.

### Modifying template:
Source files are located in separate directories in src/. The only extra-ordinary requirement for source files is that each directory in src/ is supposed to have a main.py file where the main script runs.

Message and service files are located in [ros/msg/](ros/msg) and [ros/srv/](ros/srv).

### ROS commands
In order to run ROS commands that needs to know the path to the built ROS messages and services of your project you first need to run `source scripts/registerRosMsgSrv.sh`
