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

# Run the application
python3 app.py