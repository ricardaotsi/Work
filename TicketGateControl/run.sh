#!/bin/bash
while ! pg_isready -h "db"; do
    sleep 1
done
yes | python manage.py makemigrations
python manage.py migrate
yes | python manage.py makemigrations TGCMain
python manage.py migrate TGCMain
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000