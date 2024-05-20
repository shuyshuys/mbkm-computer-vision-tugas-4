#!/bin/bash

# Check if the virtual environment exists
if [ ! -d "env" ]; then
  # Create the virtual environment
  python3 -m venv env
fi

# Activate the virtual environment
source env/bin/activate

# Install the required packages
pip install -r requirements.txt

# Pull the latest changes from the repository
git pull

# Run the application
python3 app.py