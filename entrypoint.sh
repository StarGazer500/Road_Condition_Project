#!/bin/bash

# Exit on any error
set -e

# Activate the virtual environment
source /app/venv/bin/activate

# Wait for the database to be ready
until pg_isready -h $DB_HOST -p $POSTGRES_PORT -U $POSTGRES_USER; do
  echo "Waiting for database..."
  sleep 2
done

# Apply database migrations
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createcachetable

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
fi

# Start Gunicorn with the specified configuration
gunicorn --access-logfile - --workers 3 --threads 3 --worker-connections=10 --bind unix:/var/run/gunicorn.sock Django_PM_Project.wsgi:application &

# Start Daphne
daphne -b unix:/var/run/websocket.sock Road_Condition_Project.asgi:application
