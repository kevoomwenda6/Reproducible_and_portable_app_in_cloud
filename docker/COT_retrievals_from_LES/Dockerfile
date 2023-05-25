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

RUN wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libnccl-dev_2.4.7-1+cuda10.1_amd64.deb
RUN wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libnccl2_2.4.7-1+cuda10.1_amd64.deb
RUN dpkg -i libnccl2_2.4.7-1+cuda10.1_amd64.deb
RUN dpkg -i libnccl-dev_2.4.7-1+cuda10.1_amd64.deb
RUN cp /usr/local/cuda-10.1/compat/* /usr/local/cuda/lib64/


# Install PyTorch, h5py, pyhdf, and scikit-learn
RUN pip3 install torch==1.9.0+cu102 -f https://download.pytorch.org/whl/cu102/torch_stable.html
RUN pip3 install h5py==3.1.0 pyhdf==0.10.3 scikit-learn==0.24.2
RUN pip3 install mmcv
RUN pip3 install torchinfo
RUN pip3 install matplotlib
RUN pip3 install torchvision
# Set the working directory
WORKDIR /root/
