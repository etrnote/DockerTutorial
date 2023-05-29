# Specifies the base image for the Docker container, which is python:3.9-alpine. Alpine is a lightweight Linux distribution commonly used in Docker images.
FROM python:3.9-alpine

# Sets the working directory inside the container to /app. It means that any subsequent commands will be executed in this directory.
# Think of it as mkdir + cd
WORKDIR /app


# Copies the requirements.txt file from the host machine to the current working directory (/app) inside the container.
COPY requirements.txt .

# Runs the install command to install the Python dependencies listed in the requirements.txt file using pip inside the container.
RUN pip install -r requirements.txt

# Copies all the files and directories from the current directory (the project directory on the host machine) to the current working directory inside the container (/app).
COPY . .


# Specifies the command to be executed when the container is run. In this case, it runs the Python script server.py using the Python interpreter.
CMD ["python", "server.py"]
