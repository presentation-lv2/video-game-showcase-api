#!/bin/bash

source /gameapp/etc/bin/activate
./manage.py makemigrations
./manage.py migrate
