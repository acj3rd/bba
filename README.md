# Better Bay Alliance Django Web app

This repo contains the python Django source code for the Better Bay Alliance web application.

## Run instructions

### Prerequisites
- Python version 3
- pip (make sure it is for python 3, sometimes called pip3)
- virtualenv

### Create a Virtual Enviroment
Once `virtualenv` is installed, run:
```
virtualenv venv
```

"Source" the `activate` script
```
source venv/bin/activate
```
Your virtual enviroment is now active.

### Run a local version of the webserver
To run debug local version of the wep application run:
```
python3 manage.py runserver
```
This will start a web server and the web site is viewable at `http://127.0.0.1:8000/`


