#!/bin/bash

pkill gunicorn

gunicorn -w 4 'app:app' --name PATROL-backend --daemon --log-file=./log

