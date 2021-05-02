import numpy as np
import scipy.io as scp
import os 
from PIL import Image 

home_made_path= "./datasets/images/home_made/processed/"
data_dic ={"X":[],"y":[]}

#angry
images= os.listdir(home_made_path+"angry/")
for img in images:
    image = Image.open( home_made_path+"angry/"+ img).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([0])



#fear
images= os.listdir(home_made_path+"fear")
for img in images:
    image = Image.open( home_made_path+"fear/"+ img).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([1])

#happy
images= os.listdir(home_made_path+"happy")
for img in images:
    image = Image.open( home_made_path+"happy/"+ img).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([2])


#neutral
images= os.listdir(home_made_path+"neutral")
for img in images:
    image = Image.open( home_made_path+"neutral/"+ img).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([3])

#sad
images= os.listdir(home_made_path+"sad")
for img in images:
    image = Image.open( home_made_path+"sad/"+ img).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([4])

#surprise
images= os.listdir(home_made_path+"surprise")
for img in images:
    image = Image.open( home_made_path+"surprise/"+ img).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([5])

filename = "./datasets/home_made/angry_fear_happy_neutral_sad_surprise.mat"
scp.savemat(filename, data_dic)