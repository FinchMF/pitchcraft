FROM python:3

RUN mkdir -p /pitchcraft

COPY . /pitchcraft

WORKDIR /pitchcraft

RUN pip intall -r requirements.txt 

ENTRYPOINT ["gunicorn", "app:server"] 