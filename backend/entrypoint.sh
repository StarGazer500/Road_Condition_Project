#!/bin/bash

# Exit on any error
set -e

# Activate the virtual environment
source /app/venv/bin/activate

export PYTHONPATH=/app/Road_Condition_Project


# Set environment variable for Django settings module
export DJANGO_SETTINGS_MODULE=Road_Condition_Project.core_settings.production

export DJANGO_ENV=.env.prod 

# Wait for the database to be ready
until pg_isready -h $DB_HOST -p $POSTGRES_PORT -U $POSTGRES_USER; do
  echo "Waiting for database..."
  sleep 2
done

# Apply database migrations
python ./Road_Condition_Project/manage.py migrate --noinput
python ./Road_Condition_Project/manage.py collectstatic --noinput
python ./Road_Condition_Project/manage.py createcachetable


# Start Gunicorn with the specified configuration
gunicorn --access-logfile - --workers 3 --threads 3 --worker-connections=1000 --bind 0.0.0.0:8000 Road_Condition_Project.wsgi:application
