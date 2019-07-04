# CouchDB
This is the basic CRUD operation using Python and CouchDB in Ununtu(16.04) 

1. Install python3
Open terminal via Ctrl+Alt+T or searching for “Terminal” from app launcher. When it opens, run command to add the PPA:
sudo add-apt-repository ppa:jonathonf/python-3.6

Then check updates and install Python 3.6 via commands:
sudo apt-get update
sudo apt-get install python3.6

Check the installation:
python3 -V


2. install CouchDB
Documentation
There is a documentation:
http://docs.couchdb.org/
This will help to install couchdb

3.Install python package 
pip install couchdb




How to run the code?
1. clone the files using "git clone" command.
2. Go to the CouchDb directory by typing "cd Couchdb" in your terminal.
2. Run the main.py with the json file(Here through the command line json file has been passed)
  a. If u want to create a database, then the command to run the main.py file will be:
      python3 main.py JSON/create.json
