# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Update packages and install necessary dependencies
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository universe && \
    apt-get update && \
    apt-get install unzip && \
    apt-get install -y python3 python3-pip git wget zip unzip vim curl libhdf5-serial-dev && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and setuptools
RUN pip3 install --upgrade pip setuptools wheel


# Install any needed packages specified in requirements.txt
RUN pip3 install numpy 
RUN pip3 install scikit-learn h5py 
RUN pip3 install argparse   
#RUN python3 -m pip cache purge
RUN pip3 install s3fs 
RUN pip3 install pandas 
RUN pip3 install netCDF4
 

WORKDIR /root/
