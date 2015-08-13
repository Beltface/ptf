#!/usr/bin/env python
#########################################
# Dependency check for OSX Packages
#########################################
from src.core import logging
from src.core import print_status
from src.core import print_warning
from src.core import print_error
import subprocess
import os

# this will do updates and installations
def check_dependency():
    print_status("Checking for OSX package manager...")
    if not os.path.isfile("/usr/local/bin/brew"):
        print_warning("Brew not found...")

        #Begin automated brew install
        #Check for requirements
        print_status("Checking for Xcode Command Line Tools...")
        if subprocess.Popen("xcode-select -p", shell=True).wait() != 0:
            print_warning("Xcode Command Line Tools not found...")
            print_status("Attempting install of Xcode Command Line Tools...")

            #Try to install Xcode tools
            try:
                if subprocess.Popen("xcode-select --install", shell=True).wait() == 0:
                    print_status("Xcode CLI Tools installed successfully.")
            except:
                print_error("Xcode Command Line Tool install failed. Try to install manually and rerun PTF...")
                sys.exit()

        #Pre-req test passed, begin brew installation
        try:
            print_status("Beginning brew installation..")
            subprocess.Popen("ruby -e \"$(curl -fsSL \"https://raw.githubusercontent.com/Homebrew/install/master/install)\"", shell=True).wait()
        except:
            print_error("Something in the brew installtion failed. Try to install manually and rerun PTF...")
            sys.exit()

        #install caskroom
        try:
            print_status("Beginning brew caskroom installtion and configuration")
            subprocess.Popen("brew tap caskroom/cask", shell=True).wait()
            subprocess.Popen("brew install caskroom/cask/brew-cask", shell=True).wait()
        except:
            print_error("Something in the brew caskroom installtion failed. Try to run 'brew install caskroom/cask/brew-cask' manually and rerun PTF...")
            sys.exit()