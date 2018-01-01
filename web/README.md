# CultureMania Web Service

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

* Amazon Web Server: http://18.196.2.56
* API Doc by Postman: https://documenter.getpostman.com/view/3445692/api/7Lq8gUf

## Backend Server

### Prerequisites
python2.7

### How to Setup
1. Clone this repo to your desktop: `git clone https://github.com/bounswe/bounswe2017group1.git`
2. Go to root directory of web service: `cd bounswe2017group1/web`
3. Install virtualenv: `sudo pip install virtualenv`
4. Create a virtual environment for this project: `virtualenv venv`
5. Switch to venv
    * If you are using Windows (`$ venv\Scripts\activate`)
    * If you are using UNIX (`$ source venv/bin/activate`)
6. Install necessary dependecies: `pip install -r requirements.txt`
7. Setup your own database or import database dump.
7. Run database migrations: `python manage.py migrate`
8. Run server locally: `python manage.py runserver`
9. If you get success message, server’s running, visit `http://127.0.0.1:8000/`
***

### How to Setup Database
1. Go to web service directory: `cd bounswe2017group1/web`
2. Make migrations for api app: `python manage.py makemigrations api`
3. Run migrate: `python manage.py migrate`
4. Create admin user: `python manage.py createsuperuser`

### How to Use
1. Switch to venv
    * If you are using Windows (`$ venv\Scripts\activate`)
    * If you are using UNIX (`$ source venv/bin/activate`)
2. Install necessary dependecies: `pip install -r requirements.txt`
3. Setup your own database or import database dump.
4. Run database migrations: `python manage.py migrate`
5. Run server locally: `python manage.py runserver`
6. If you get success message, server’s running, visit `http://127.0.0.1:8000/`
***

### How to Test
1. Install [Postman](https://www.getpostman.com) app
2. Import [api collection](https://raw.githubusercontent.com/bounswe/bounswe2017group1/master/web/api.postman_collection.json) or use "Run in Postman" in [documentation](https://documenter.getpostman.com/view/3445692/api/7Lq8gUf)

## Frontend Server

### Prerequisites
node.js, npm

### How to Usage
1. Go to frontend project folder: `cd bounswe2017group1/web/frontend`
2. Install necessary dependecies: `npm install`
3. Run server locally: `npm start`
4. If you get success message, server’s running, visit `http://127.0.0.1:3000/`
***

## Annotation Server

### Prerequisites
python2.7, mongodb

### How to Setup
1. Clone this repo to your desktop: `git clone https://github.com/bounswe/bounswe2017group1.git`
2. Go to annotation service folder: `cd bounswe2017group1/web/annotation_jsonld`
3. Install necessary dependecies: `pip install -r requirements.txt`
4. Start mongodb service: `mongod`
5. Create a new mongo database: `mongo <dbname>`
6. Run annotation server locally: `python server.py`
7. If you get success message, server’s running, visit `http://127.0.0.1:5005/`
***
