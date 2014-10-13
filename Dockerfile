# DocBox
FROM python:2-onbuild

MAINTAINER Nathan Yergler <nathan@yergler.net>

RUN apt-get install build-essential
VOLUME /docs

CMD [ "python", "docbox.py" ]
