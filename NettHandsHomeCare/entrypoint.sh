#!/bin/bash
python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn NettHandsHomeCare.wsgi:application --bind "127.0.0.1:8000" 