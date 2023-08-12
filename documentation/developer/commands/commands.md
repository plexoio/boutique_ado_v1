# Commands Used
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