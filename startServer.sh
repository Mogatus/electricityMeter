#!/bin/bash

source /home/jojo/devel/electricityMeter/my_venv/bin/activate
export FLASK_APP=electricityServer
export FLASK_ENV=development
<<<<<<< HEAD
flask run --host=0.0.0.0
=======
flask run --host=0.0.0.0
>>>>>>> c0302c1 (shell scripts for collecting data and starting flask server)
