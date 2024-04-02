#!/bin/bash

# Stop the current Django server
sudo systemctl stop gunicorn

# Activate your virtual environment (if any)
source .venv/Scripts/activate

# Navigate to your project directory
# cd /path/to/your/project

# Pull the latest changes from your Git repository
git pull

# Install or update Python dependencies
pip3 install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Migrate database changes
python3 manage.py migrate

# Restart the Django server
sudo systemctl start gunicorn
