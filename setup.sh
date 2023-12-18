#!/bin/bash

# Update the package lists for upgrades and new package installations
sudo apt-get update -y

# Install Python3 and pip3
sudo apt-get install python3 python3-pip -y

# Install wget, curl, zip and unzip
sudo apt-get install wget curl zip unzip -y

# Install fabric library for Python
pip3 install fabric
