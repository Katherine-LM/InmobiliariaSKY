#!/usr/bin/env bash
# Exit on error
set -o errexit

# Debugging
echo "Current directory:"
pwd
echo "List of files in current directory:"
ls -la
echo "List of files in inmobiliaria directory:"
ls -la inmobiliaria

# Install dependencies
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate