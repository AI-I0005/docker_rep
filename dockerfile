# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app

# Install the required packages from requirements.txt
RUN pip install -r requirements.txt

# Command to run the Flask application (assuming your app logic is in flask_app.py)
CMD ["python", "flak_app.py"]
