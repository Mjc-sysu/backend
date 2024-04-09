#!/bin/bash

pkill gunicorn

~/.local/bin/gunicorn -w 4 'app:app' --name PATROL-backend --daemon --log-file=./log
