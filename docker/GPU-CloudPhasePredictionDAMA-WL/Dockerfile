# Use the latest Ubuntu image
FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

CMD nvidia-smi

# Update packages and install necessary dependencies
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository universe && \
    apt-get update && \
    apt-get install -y python3 python3-pip git wget zip unzip vim curl libhdf5-serial-dev && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and setuptools
RUN pip3 install --upgrade pip setuptools wheel

# Install any needed packages specified in requirements.txt
#RUN pip3 install numpy 
#RUN pip3 install scikit-learn h5py 
#RUN pip3 install argparse   


RUN wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libnccl-dev_2.4.7-1+cuda10.1_amd64.deb
RUN wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libnccl2_2.4.7-1+cuda10.1_amd64.deb
RUN dpkg -i libnccl2_2.4.7-1+cuda10.1_amd64.deb
RUN dpkg -i libnccl-dev_2.4.7-1+cuda10.1_amd64.deb
RUN cp /usr/local/cuda-10.1/compat/* /usr/local/cuda/lib64/

#RUN wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnccl-dev_2.8.3-1+cuda11.2_amd64.deb
#RUN wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnccl2_2.8.3-1+cuda11.2_amd64.deb

#RUN dpkg -i libnccl-dev_2.8.3-1+cuda11.2_amd64.deb
#RUN dpkg -i libnccl2_2.8.3-1+cuda11.2_amd64.deb


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