#!/usr/bin/env python

import subprocess

def main():
    # Navigate to your Django project directory
    project_dir = '/coded'
    subprocess.run(['cd', project_dir], check=True, shell=True)

    # Activate virtualenv
    venv_activate = '/.venv/Scripts/activate'
    subprocess.run(['source', venv_activate], check=True, shell=True)

    # Pull the latest changes from the Git repository
    subprocess.run(['git', 'pull', 'origin', 'main'], check=True)

    # Collect static files (if necessary)
    subprocess.run(['python', 'manage.py', 'collectstatic', '--noinput'], check=True)

    # Migrate the database
    subprocess.run(['python', 'manage.py', 'migrate'], check=True)

    # Restart the development server (assuming you're using Gunicorn)
    subprocess.run(['systemctl', 'restart', 'gunicorn'], check=True)

if __name__ == '__main__':
    main()
