FROM ubuntu:22.04

WORKDIR /opt

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install flask

COPY app.py /opt/app.py

EXPOSE 8080

CMD ["python3", "/opt/app.py"]
