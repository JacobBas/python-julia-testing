# import the base image for julia 1.7.2
FROM julia:1.7.2-buster as julia_builder
WORKDIR /src
ADD . .


# import the base image for python 3.9.10
FROM python:3.9.10-slim-buster as python_builder
WORKDIR /src
ADD . .
RUN python3 -m pip install -r requirements.txt

# making sure that we retain the julia build step
COPY --from=julia_builder /usr/local/julia /usr/local/
# RUN julia --project=. -e "using Pkg; Pkg.resolve()" 
RUN julia --project=. -e "using Pkg; Pkg.instantiate()" 

# final command to run to open the container
# with an interactive shell
CMD [ "bash" ]
