FROM giovtorres/docker-centos7-slurm:latest AS build

# Add mockHPC app to slurm image
RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN python3.8 -m pip install --upgrade pip
RUN python3.8 -m pip install -r requirements.txt
