# backend of PATROL
[![Push-to-EC2](https://github.com/csci-578-group-project/backend/actions/workflows/github-actions-ec2.yml/badge.svg?event=push)](https://github.com/csci-578-group-project/backend/actions/workflows/github-actions-ec2.yml)

This is a flask application providing RESTful APIs.

Environment: python 3

## run
step 1. install dependencies
```sh
pip install -r requirements.txt
```

step2. run the project in development mode
```sh
python app.py
```

The documented API can be found under `http://localhost:5001`.


## code structure
[Best practice by flask-RestX](https://flask-restx.readthedocs.io/en/latest/scaling.html)

