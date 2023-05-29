# base image for the Docker container, which is postgres:12. It pulls the official PostgreSQL image with version 12.
FROM postgres:12


# set environment variables inside the container. 
# POSTGRES_USER, POSTGRES_PASSWORD, and POSTGRES_DB are environment variables used by PostgreSQL to set up the database user, password, and database name, respectively.
ENV POSTGRES_USER=dbuser
ENV POSTGRES_PASSWORD=dbpassword
ENV POSTGRES_DB=messages


# copies the init.sql file from the host machine to the /docker-entrypoint-initdb.d/ directory inside the container. 
# The files in this directory are automatically executed when the PostgreSQL container is initialized, 
# allowing you to set up the initial database schema or perform any required initialization steps.
COPY init.sql /docker-entrypoint-initdb.d/
