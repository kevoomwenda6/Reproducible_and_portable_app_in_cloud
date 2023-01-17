FROM python

RUN pip install torch
RUN pip install numpy
RUN pip install sklearn
RUN pip install scikit-learn

COPY training_data ./training_data
COPY data_utils.py ./data_utils.py
COPY model.py ./model.py
COPY train.py ./train.py

RUN python train.py --training_data_path="./training_data"  --model_saving_path="./"
