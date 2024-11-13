import torch
import cv2
from IPython import display as ipythondisplay
from torch import nn

from tqdm.autonotebook import tqdm
from transformers import AutoTokenizer, AutoModel
from transformers import DistilBertModel, DistilBertConfig, DistilBertTokenizer
import albumentations as A
import cv2
import gc
import itertools
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import time
import timm
import torch
import torch.nn.functional as F

class CFG:
    debug = False

    image_path = "/Users/himangshudeka/Desktop/DL_DATASET_PROJECT/ROCOv2/train"
    captions_path = "/Users/himangshudeka/Desktop/DL_DATASET_PROJECT/ROCOv2"
    batch_size = 12
    num_workers = 2
    head_lr = 1e-3
    image_encoder_lr = 1e-4
    text_encoder_lr = 1e-5
    weight_decay = 1e-3
    patience = 1
    factor = 0.8
    epochs = 2
    trained_model = 'clinical_bert_weights.pt'
    saved_model_clinical = 'weights.pt'
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_name = 'resnet50'
    image_embedding = 2048
    text_encoder_model = "distilbert-base-uncased"
    clinical_encoder_model = "emilyalsentzer/Bio_ClinicalBERT"
    text_embedding = 768
    text_tokenizer = "distilbert-base-uncased"
    max_length = 200
    pretrained = True
    trainable = True
    temperature = 1.0
    size = 224
    num_projection_layers = 1
    projection_dim = 256
    dropout = 0.1