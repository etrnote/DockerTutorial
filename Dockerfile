
# Specifies the base image for our Docker image. In this case, we're using the official Python 3.9 slim image.
FROM python:3.9-slim


# Sets the working directory inside the container to /app. This is where our Python script will be copied.
WORKDIR /app

# Copies the script.py file from the host (your local machine) to the current directory inside the container.
COPY script.py .


# Specifies the command to run when the container starts. In this case, it executes the Python script.
CMD ["python", "script.py"]