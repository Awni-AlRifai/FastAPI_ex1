# pull official base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory
WORKDIR /app
# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . . 
#shell command
# CMD "sh"
EXPOSE 8004