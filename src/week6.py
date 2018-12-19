import cv2
import numpy as np
import os
from sklearn.utils import shuffle
import torch

nrows = 128
ncols = 128

def process_image(imagepath):
	img = cv2.resize(cv2.imread(imagepath,cv2.IMREAD_COLOR), (nrows,ncols), interpolation = cv2.INTER_CUBIC)
	return img/255