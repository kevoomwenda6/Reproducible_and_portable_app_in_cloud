# Use the latest Ubuntu image
FROM ubuntu:latest

CMD nvidia-smi

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


# Update the package list and install required packages
RUN apt-get update -y && \
    apt-get install -y ssh && \
    apt-get install -y git && \
    apt-get install -y wget && \
    apt-get install -y curl && \
    apt-get install -y libglib2.0-0 && \
    apt-get install -y libsm6 && \
    apt-get install -y libxrender1 && \
    apt-get install -y libxext6 && \
    apt-get install -y libgl1-mesa-glx && \
    apt-get install -y libxml2-dev && \
    apt-get install -y libxslt-dev && \
    apt-get install -y python3-dev && \
    apt-get install -y build-essential && \
    apt-get install -y libhdf5-dev && \
    apt-get install -y libhdf5-serial-dev && \
    apt-get install -y libhdf5-103 && \
    apt-get install -y libpq-dev && \
    apt-get install -y libssl-dev && \
    apt-get install -y libffi-dev && \
    apt-get clean


# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda &&\
     rm ~/miniconda.sh

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

# Create a conda environment
RUN conda create -n cloud-phase-prediction-env -c conda-forge python=3.7 pytorch h5py pyhdf 

# Set the default conda environment
SHELL ["/bin/bash", "-c"]
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate cloud-phase-prediction-env" >> ~/.bashrc


WORKDIR /root/