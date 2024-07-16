# Private-Chat-Django
This is Web Application for online messaging. This project is based on Django Channels and TailWindCSS and uses Django ASGI_APPLICATION and Django WebSocket for the messaging connection.  Database is Django default database i.e. SQLite

#Work Flow : at the very beging of the project first of all virtual environment is created by running  the vs code terminal or cmd terminal : pip install virtualenv
#Create virtual environment for the project by running the command : virtual privatechat_env
#Activate the virtual environment by the cmnd : 
    for windows: .\privatechat_env\Scripts\Activate 
    for linux, mac : source privatechat_env/bin/activate
#Install Django latest version in that virtual env by cmd: pip install django channels
#create the project by cmd: django-admin startporject privatechat
#change the cmd directory by: cd privatechat
#creeate core project by cmd: python manage.py startapp core
#once project is setup successfully insatll daphne package in the virtual env directory;  HTTP, HTTP2, and WebSocket protocol server for ASGI and ASGI-HTTP, developed as part of the Django Channels project.
    run cmd to install daphne: pip install daphne
#run the project by cmd: python manage.py runserver
#press ctrl + right click on local hosted https:/ urls
#once the project is running on web browser then terminate the terminal by cmd: ctrl + C
#run cmd to activate the daphne: daphne -p 8000 privatechat.asgi:application
