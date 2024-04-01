#!/usr/bin/env python

import subprocess

# Array of commands
commands = [
    'echo $PWD',
    'whoami',
    'git pull',
    'git status',
    'git submodule sync',
    'git submodule update',
    'git submodule status'
]

# Execute commands
output = ''
for command in commands:
    tmp = subprocess.run(command, shell=True, capture_output=True, text=True)
    output += f"<span style=\"color: #6BE234;\">$</span><span style=\"color: #729FCF;\">{command}\n</span><br />"
    output += f"{tmp.stdout}\n<br /><br />"

# HTML output
html_output = f'''
<!DOCTYPE HTML>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <title>GIT DEPLOYMENT SCRIPT</title>
</head>
<body style="background-color: #000000; color: #FFFFFF; font-weight: bold; padding: 0 10px;">
<div style="width:700px">
    <div style="float:left;width:350px;">
    <p style="color:white;">Git Deployment Script</p>
    {output}
    </div>
</div>
</body>
</html>
'''

print(html_output)
