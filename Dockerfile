# import the base image for julia 1.7.2
FROM julia:1.7.2-buster as julia_builder
WORKDIR /src

# import the base image for python 3.9.10
FROM python:3.9.10-slim-buster as python_builder
WORKDIR /src
ADD . .
ADD requirements.txt /src
RUN python3 -m pip install -r requirements.txt

# making sure that we retain the julia build step
COPY --from=julia_builder /usr/local/julia /usr/local/

# final command to run to open the container
# with an interactive shell
CMD [ "bash" ]
