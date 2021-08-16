FROM python:3.8

WORKDIR /app

RUN apt-get update 
RUN apt-get -y install libgl1-mesa-glx

RUN pip3 install matplotlib
RUN pip3 install pandas
RUN pip3 install numpy
RUN pip3 install tqdm
RUN pip3 install mediapipe==0.8.3
RUN pip3 install wget
# RUN pip3 install zipfile
