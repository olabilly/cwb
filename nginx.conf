#!/bin/bash

# Command to activate the virtual environment
command='/var/www/html/.venv/Scripts/activate'

# Python path for your Django project
pythonpath='/var/www/html/coded'

# Bind address for Gunicorn
bind='164.92.83.205:8000'

# Number of Gunicorn workers
workers=3

# Activate the virtual environment
source $command

# Navigate to your project directory
cd $pythonpath

# Stop the current Django server
sudo systemctl stop gunicorn

# Pull the latest changes from your Git repository
git pull

# Install or update Python dependencies
pip3 install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Migrate database changes
python3 manage.py migrate

# Restart the Django server with Gunicorn
gunicorn coded.wsgi:application --bind $bind --workers $workers
