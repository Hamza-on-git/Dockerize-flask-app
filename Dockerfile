# Getting the base image
FROM python:3.9

# Working directory for app
WORKDIR app/

#copy the code from the system
COPY app.py .

#Install the requred libraries
RUN pip install Flask

# Run the application
CMD [ "python", 'app.py' ]
