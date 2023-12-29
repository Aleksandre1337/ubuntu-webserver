
  

# Web Server Setup Project

  

  

This project consists of a bash script and a Python script (using Fabric) that automate the process of setting up a web server and deploying a template website on an Ubuntu server.

  

  

## Bash Script

  

  

The bash script (`setup.sh`) prepares the Ubuntu server by installing the necessary packages. It performs the following tasks:

  

  

1. Updates the package lists for upgrades and new package installations.

  

2. Installs Python3 and pip3.

  

3. Installs wget, curl, zip, and unzip.

  

4. Installs the Fabric library for Python.

  

  

To run the bash script, use the following command:

  

  
  
  

./setup.sh

  

  

## Fabric Script

  

The Fabric script (fabfile.py) automates the process of setting up the web server and deploying the website. It performs the following tasks:

  

  

1. Installs apache2, wget, and unzip.

  

2. Starts and enables the apache2 service.

  

3. Downloads and unzips the website template.

  

4. Moves the website files to the appropriate directory.

  

5. Restarts the apache2 service.

  

  

To run the Fabric script, use the following command:

  

  

fab websetup **WEBURL** **DIRNAME**

  
  

  

Replace **WEBURL** with the URL of the website template and **DIRNAME** with the name of the directory where the website files should be placed.

According to the template which is used in this script, the command will be the following:

fab web-setup https://www.tooplate.com/zip-templates/2121_wave_cafe.zip 2121_wave_cafe

Website design by - **Tooplate**
