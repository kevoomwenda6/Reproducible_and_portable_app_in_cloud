FROM ubuntu:20.04

RUN apt update && apt install software-properties-common -y

RUN apt-get install -y python3-pip
RUN apt-get install -y git wget zip unzip vim curl

RUN pip3 install pandas sklearn numpy h5py

RUN pip3 install datetimerange pyhdf netCDF4 cftime s3fs

#for dask
RUN pip3 install dask dask_jobqueue distributed 

WORKDIR /root/
