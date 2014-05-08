#!/usr/bin/python
import subprocess
import sys
import os

def check(cmd):
    sys.stdout.write('> %s' % cmd)
    sys.stdout.flush()
    subprocess.check_output(cmd, shell=True)

def install(cmd):
    check('sudo apt-get install -qq -y %s' % cmd)

check('python --version')
check('sudo apt-get update')
install('git')
install('gcc')
install('xvfb')
install('libqt4-dev')
install('python-pip')
install('python-pyside')
install('python-qt4')
check('pip -q install pytest')
if not os.path.isdir('pytest-qt'):
    check('git clone https://github.com/nicoddemus/pytest-qt.git')
