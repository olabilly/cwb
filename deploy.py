#!/usr/bin/env python

import subprocess

def main():
    # navigate to your django project directory
    project_dir = '/coded'
    subprocess.run(['cd', project_dir], check=True)

    #Activate virtualenv
    venv_activate = '/.venv/Scripts/activate'
    subprocess.run(['source', venv_activate], check=True, shell=True)

    # pull the latest change from the git repository
    subprocess.run(['git', 'pull', 'origin','main'], check=True)

    # collect static files ( if necessary)
    subprocess.run(['python','manage.py', 'collectstatic', '--noinput'], check=True)

    #migrate the database
    subprocess.run(['python','manage.py','migrate'], check=True)

    # Restart the development server
    subprocess.run(['systemct1', 'restart', 'gunicorn'], check=True)

if __name__ == '__main__':
    main()
