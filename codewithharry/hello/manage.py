#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# pip install djnago
# django-admin startproject hello
# python manage.py runserver
# python manage.py
# python manage.py startapp home
# add urls.py in home

#54:38, 1:17:48 ,1:33:03

# python manage.py makemigrations
# python manage.py migrate       
# python manage.py createsuperuser 
# python manage.py makemigrations 
# import and register admin

# home k HomeConfig ko copy kerkey hello k settings m installed app m dena h 
# per python manage.py makemigrations
# per table banan h
# python manage.py migrate