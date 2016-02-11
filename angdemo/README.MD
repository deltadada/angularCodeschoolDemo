FROM TUTORIAL:

campus.codeschool.com/courses/shaping-up-with-angular-js/



FIRST STEPS

django-admin startproject angdemo 
cd angdemo
python manage.py startapp gemstore
python manage.py runserver
python manage.py makemigrations gemstore
python manage.py migrate

python manage.py inspectdb

python manage.py loaddata initial_data


Loads db with initial data from angdemo/gemstore/fixtures/initial_data.json
python manage.py loaddata initial_data



cd C:\gitrepo\angular_demo\django_angdemo\angdemo\
python manage.py runserver  