# Docker Tutorial

## Steps

1. Create a Project Directory
   Create a new directory for your project. Open CMD and navigate to your directory, and create a new folder.

2. Create a Python script
   it can be as simple as  

   ```python
   print("Hello Docker!")
   ```

    run it locally to make sure it works.

3. Create a new file named `Dockerfile` in the project directory. This file defineds the instructions to build a Docker image.

    ```docker

    # Specifies the base image for our Docker image. In this case, we're using the official Python 3.9 slim image.
    FROM python:3.9-slim


    # Sets the working directory inside the container to /app. This is where our Python script will be copied.
    WORKDIR /app

    # Copies the script.py file from the host (your local machine) to the current directory inside the container.
    COPY script.py .


    # Specifies the command to run when the container starts. In this case, it executes the Python script.
    CMD ["python", "script.py"]
    ```

4. Build the Docker Image
    Run the following commands:

    ```bash
    docker build -t python-docker-tutorial .
    ```

    ! notice the `.` at the end, it's a part of the command, it means build the image from the Dockerfile in this directory.
    The `-t` flag tags the image with the given name (`python-docker-tutorial` in this case)

    Run `docker images` to see if the image was created successfully

5. Run the Docker Container
    To run the Docker container 

    ```bash
    docker run  python-docker-tutorial
    ```
    
    Since the script terminates, the container will shut down once the execution is complete.
    To see a list of all containers (including stopped ones):
    `docker ps -a`

6. Run the Docker Container Interactively
   To run the Docker container interactively and execute the Python shell inside it, use the following command:
   ```bash
   docker run -it python-docker-tutorial python
    ```
    The -it flag runs the container in interactive mode and attaches your terminal to the container's standard input and output. python specifies the command to run inside the container (the Python shell).