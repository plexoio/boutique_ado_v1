# Commands Used

## General

- `import os` at settings.py
- `python3 manage.py runserver`
## Project Setup

- `pip3 install 'django<4'` - Django 3.2 is the LTS (Long Term Support) version of Django and is therefore preferable to use over the newest Django 4
- `django-admn startproject boutique_ado .` - Start project
- `touch .gitignore` - add:
    - `*.spqlite3`
    - `*.pyc`
    - `__pycache__/`
- python3 manage.py makemigrations --dry-run
- python3 manage.py migrate --plan
- python3 manage.py migrate
- python3 manage.py createsuperuser
- git status
- git remote -v

## Authentication System
- `pip3 install django-allauth==0.41.0`
- Instructions: https://www.youtube.com/watch?v=pwmJLp2jots & https://www.youtube.com/watch?v=TmdKjjnGWyo
- Docs: https://django-allauth.readthedocs.io/en/latest/installation.html

## Requirements.txt

- `pip3 freeze > requirements.txt`

## Make templates

- `mkdir templates`
- `mkdir templates/allauth`
- `ls ../.pip-modules/lib` - determine version
- `cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/` - recursive copy of allauth templates

## Start First App