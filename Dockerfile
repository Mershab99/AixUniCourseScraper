FROM python:3
WORKDIR ./
#COPY requirements.txt ./
RUN pip install selenium
COPY ./ ./