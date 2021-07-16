FROM python:3.7.3-alpine
RUN apk add --no-cache --update bash libxslt libxslt-dev libffi-dev linux-headers alpine-sdk build-base \
                                curl-dev libressl-dev
ENV DEPLOY_PATH=/var/www/kifaco
RUN mkdir -p $DEPLOY_PATH

WORKDIR $DEPLOY_PATH

COPY kifaco $DEPLOY_PATH/kifaco

COPY Pipfile $DEPLOY_PATH/Pipfile
COPY Pipfile.lock $DEPLOY_PATH/Pipfile.lock
COPY Makefile $DEPLOY_PATH/Makefile
COPY kifaco.py $DEPLOY_PATH/cs_globalsdp_front.py

RUN make install