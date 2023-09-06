# HuRobotic Backend


## Install and Run

Make sure you have **Python 3.x** installed and **the latest version of pip** *installed* before running these steps.

Clone the repository using the following command

```bash
gh repo clone https-github-com-HuRoboticWebsite/HuRobotic_backend
# After cloning, move into the directory having the project files using the change directory command
cd HuRobotic_backend
```
Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python -m venv env
```
Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```
Install all the project Requirements
```bash
pip install -r requirements.txt
```
-Apply migrations and create your superuser (follow the prompts)

```bash
# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser
```

Run the development server

```bash
# run django development server
python manage.py runserver
```
