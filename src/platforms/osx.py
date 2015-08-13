#!/usr/bin/env python
#########################################
# Core installation for OSX Packages
#########################################
import subprocess
from os import stat
from pwd import getpwuid
from src.core import logging

# this will do updates and installations
def base_install_modules(module_name):

	# get brew usernames
	brew_usr = getpwuid(stat(subprocess.check_output("which brew", shell=True).rstrip()).st_uid).pw_name

    # will work for 1 or more space- or comma-separated modules
    modules = module_name.replace(",", " ")
    command = "\"su - %s -c brew install -y " + modules + "\""
    subprocess.Popen(command, shell=True).wait()