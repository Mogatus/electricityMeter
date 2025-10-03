# Electricity Meter

A simple programm, that collects data from a Hansol ESS AIO, stores the data in a MariaDB an displays it a web page.

Components:
* main.py: collects data of the day and stores it in database. Can be run with cron at the end of the day. See startCollect.sh.
* meterData.py: Data structure for the meter data
* electricityServer.py: Start a (very, very simple) flask application that return the stored data as a web page
* startServer.sh: Starts the flask app and keeps running until ended by user.
* startCollect.sh: Executes main.py. Can be placed in cron tab near end of day.
* requirements.txt: Textfile with environment info. Environment can be set up with: pip3 install -r ./requirements.txt

Starting server with gunicorn:
screen -S electricityServer gunicorn -w 2 -b 0.0.0.0:8000 electricityServer:app

