FROM python:3.9.18-slim

COPY . /proj
RUN python3 -m pip install -r /proj/requirements.txt && rm -rf /proj/requirements.txt
WORKDIR /proj
