FROM mcr.microsoft.com/playwright/python:v1.55.0-noble
# may have to change to version 1.50.0
WORKDIR /app
# I dont what this does yet

COPY requirements.txt /superbugfinder/
COPY webpages /superbugfinder/pages
COPY tests /superbugfinder/tests
COPY utilities /superbugfinder/utilities
COPY AutTBS /superbugfinder/AutTBS

RUN pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir -r /superbugfinder/requirements.txt

RUN playwright install chromium firefox webkit

WORKDIR /superbugfinder
