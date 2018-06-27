
# Update UBUNTU distro
sudo apt-get upgrade

# Install git
sudo apt install git
sudo apt install libnss3
sudo apt install chromium-browser
sudo apt install xvfb
sudo apt install ffmpeg

# Install python's package manager
sudo apt install python-pip
pip install --upgrade pip

# Install a virtual env
pip install virtualenv
virtualenv .env
source .env/bin/activate
## To get out of virtualenv environment just "deactivate"
## All instances of "sudo" excecutions of python go back to global env

# Insall python packages into the virtual env (use requirements in the future)s
pip install lettuce
pip install selenium
pip install nose
pip install pyvirtualenv
pip install python-Levenshtein
## Install phantomjs 
## this does not work: sudo apt-get install phantomjs
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
## Untar it
tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2
## Moved the phantomjs executable to /usr/local/bin/ (may need sudo)
sudo cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/


# Clone github repository
# git clone https://github.com/mobomo/dcrb-mssa-atests.git 
# user: automatedtests@mobomo.com
# pasw: mobomo2017
# TODO: make shure drivers and corresponding browsers are present


# INSTALL ECLIPSE
# sudo apt install eclipse
# sudo apt install sudo sudo add-apt-repository ppa:openjdk-r/ppa
# sudo apt-get install openjdk-8-jdk
# sudo apt-get install openjdk-8-source #this is optional, the jdk source code
# apt-cache search jdk
# export JAVA_HOME=/usr/lib/jvm/java-8-openjdk
# export PATH=$PATH:/usr/lib/jvm/java-8-openjdk/bin
# javac -version
