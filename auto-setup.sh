#!/bin/bash

# This version of the script will automatically accept the default answers to any prompts that the package manager `apt-get` might display, therefore, the manual input from the user will not be required

# Update the package lists for upgrades and new package installations
sudo DEBIAN_FRONTEND=noninteractive apt-get update -y

# Install Python3 and pip3
sudo DEBIAN_FRONTEND=noninteractive apt-get install python3 python3-pip -y

# Install wget, curl, zip and unzip
sudo DEBIAN_FRONTEND=noninteractive apt-get install wget curl zip unzip -y

# Install fabric library for Python
pip3 install fabric
