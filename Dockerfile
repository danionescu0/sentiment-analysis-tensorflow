FROM python:3.6-buster

#clone the application
WORKDIR /root
RUN git clone https://github.com/danionescu0/sentiment-analysis-tensorflow.git sa
WORKDIR /root/sa
RUN pip install -qr requirements.txt

EXPOSE 8001
