FROM ubuntu:20.04

RUN apt update && apt install software-properties-common -y

RUN apt-get install -y python3-pip
RUN apt-get install -y git wget zip unzip vim curl

RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install wheel

RUN python3 -m pip install --upgrade pip setuptools
RUN python3 -m pip install configargparse
RUN python3 -m pip install netCDF4 h5py pyhdf pandas numpy datetimerange sklearn

RUN python3 -m pip install matplotlib seaborn tables pvlib

#for dask
RUN python3 -m pip install "dask[complete]"
RUN python3 -m pip uninstall -y click
RUN python3 -m pip install dask-ml click==7

WORKDIR /root/
