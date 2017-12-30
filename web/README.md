# CultureMania Web Service
***
Our API base url is [http://18.196.2.56](http://18.196.2.56)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites
python2.7

## How to Setup
1. Clone this repo to your desktop: `git clone https://github.com/bounswe/bounswe2017group1.git`
2. Go to root directory of web service: `cd bounswe2017group1/web`
3. Install virtualenv: `pip install virtualenv`
4. Create a virtual environment for this project: `virtualenv venv`
5. Switch to venv
    - If you are using Windows (`$ venv\Scripts\activate`)
    - If you are using UNIX (`$ source venv/bin/activate`)
6. Install necessary dependecies: `pip install -r requirements.txt`
7. Run database migrations: `python manage.py migrate`
8. Run server locally: `python manage.py runserver`
9. If you get success message, server’s running, visit `http://127.0.0.1:8000/`
***

Go to http://127.0.0.1:8000 and see if it works

Use API on http://127.0.0.1:8000/api base.

***
