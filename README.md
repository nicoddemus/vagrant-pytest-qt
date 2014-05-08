# vagrant-pytest-qt #

Experiment using vagrant to bring up a development VM ready to work on pytest-qt

## Usage ##

1. Install [VirtualBox](https://www.virtualbox.org/) and [vagrant](www.vagrantup.com), following platform specific instructions.

2. Start up the virtual machine and wait up a little:

  vagrant up

3. ssh into the machine:

  vssh.bat

4. startup X

  startx
  
5. In another ssh session, run the tests:

  cd pytest-qt
  DISPLAY=99.0 py.test




