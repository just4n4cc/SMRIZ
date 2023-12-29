FROM python:3.9.18-slim

COPY . /proj
RUN python3 -m pip install -r /proj/requirements.txt && rm -rf /proj/requirements.txt
RUN apt-get update && apt install -y git
WORKDIR /proj
