#!/bin/bash

source /home/jojo/devel/electricityMeter/my_venv/bin/activate
export FLASK_APP=electricityServer
export FLASK_ENV=development
flask run --host=0.0.0.0