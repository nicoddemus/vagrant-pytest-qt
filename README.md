# vagrant-pytest-qt #

Experiment using vagrant to bring up a development VM ready to work on pytest-qt

## Usage ##

* Install [VirtualBox](https://www.virtualbox.org/) and [vagrant](www.vagrantup.com), following platform specific instructions.

* Start up the virtual machine and wait up a little:

```
  vagrant up
```  

* ssh into the machine:

```
  vssh.bat
```  

* startup X

```
  startx
```

* In another ssh session, run the tests:

```
  cd pytest-qt
  DISPLAY=99.0 py.test
```




