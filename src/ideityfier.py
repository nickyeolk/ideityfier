import matplotlib.pyplot as plt
import torch
import numpy as np
import torch.nn as nn
# import src.week6 as wk6
from torch.utils.data import Dataset, DataLoader, TensorDataset
import torchvision.transforms as transforms
import torchvision.transforms.functional as TF
import requests
from io import BytesIO
import cv2
from scipy import misc

class Ideityfier():
	"""This creates the ideityfier class. It takes in the url to 
	a .jpg image and returns the name of the deity."""
	def __init__(self):
		# set up model
		self.weights = torch.load('./data/model_weights.pt', map_location='cpu')
		self.convnet = torch.load('./data/model.pt', map_location='cpu')
		self.convnet.load_state_dict(self.weights)
		self.convnet.eval()
		self.labels = ['Mercy', 'Happy', 'Monkey']

	def process_raw(self, image_path):
		nrows = 128
		ncols = 128
		req = requests.get(image_path)
		img = misc.imread(BytesIO(req.content))
		imp = cv2.resize(img, (nrows,ncols), interpolation = cv2.INTER_CUBIC)
		imp = imp/255
		inp2 = np.moveaxis(imp,-1,0)
		return inp2

    # Predictor
	def predict(self, image_url):
	    inp = self.process_raw(image_url)
	    test_img = TensorDataset(torch.from_numpy(inp).float())
	    output = self.convnet(test_img.__getitem__())
	    print(output)
	    _, predicted = torch.max(output.data, 1)
	    return self.labels[predicted.item()]

# Set up data input stream
class TensorDataset(Dataset):
    def __init__(self, tensor):
        self.tensor = tensor
        self.resize = transforms.Resize(size=(224,224))
    def __getitem__(self):
        out = self.tensor
        out = TF.to_pil_image(out)
        out = self.resize(out)
        out = TF.to_tensor(out).unsqueeze_(0)
        return out
    def __len__(self):
        return self.tensor.size(0)

ideityfier = Ideityfier()

