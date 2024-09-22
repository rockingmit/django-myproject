Django Run Command
----------------------------------------------------------------
Framwork Used :
    pip install django
    pip install django-rest-framework

Run Server Command :
    python manage.py runserver
    python manage.py createsuperuser

Dockerization : 
----------------------------------------------------------------
sudo docker build -t myproject .
sudo docker run -it -p 8000:8000 \
     -e DJANGO_SUPERUSER_USERNAME=admin \
     -e DJANGO_SUPERUSER_PASSWORD=admin \
     -e DJANGO_SUPERUSER_EMAIL=admin@admin.com \
     myproject