FROM python:3.10-slim-bullseye

LABEL maintainer="Luis Rodrigues <larpig@gmail.com>"
LABEL version="0.1"
LABEL description="Text Classification using \
                  Kaggle Consumer Complaints Dataset \
                  Scikit-learn TF-IDF \
                  XBGoost Classifier \
                  Kedro \
                  Pytest \
                  FastAPI \
                  Uvicorn \
                  Docker."

ARG REQUIREMENTS_PATH="./src/requirements.in"
ENV REQUIREMENTS_PATH=$REQUIREMENTS_PATH
ARG ENTRYPOINT_PATH="./entrypoint.sh"
ENV ENTRYPOINT_PATH=$ENTRYPOINT_PATH

WORKDIR /

COPY $REQUIREMENTS_PATH /requirements.txt

RUN apt update &&\
    pip install pip --upgrade &&\
    pip install --no-cache-dir -r ./requirements.txt && \
    mkdir -p /tmp/logs/

COPY . .

RUN pip install -e ./src/. && \
    chmod +x $ENTRYPOINT_PATH

ENTRYPOINT $ENTRYPOINT_PATH
