# import the base image for python 3.9.10
FROM python:3.9.10-slim-buster

# set the working directory to the image
WORKDIR /src

# adding all of the poject files into the image
ADD . .

# loading in the required dependencies
ADD requirements.txt /src
RUN pip install -r requirements.txt

# final command to run to open the container
# with an interactive shell
CMD [ "bash" ]
