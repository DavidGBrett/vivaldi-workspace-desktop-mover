# Handy script to run the current version of the project

# This assumes you have already created a python virtual environment,
# named venv, in the project root directory.

# relative to the script location
$ProjectRoot = Split-Path -Parent $PSScriptRoot

# activate the python virtual environment
Set-Location $ProjectRoot
.\venv\Scripts\Activate.ps1

# run cli.py
Set-Location .\src
python -m vivaldi_workspace_desktop_mover.cli