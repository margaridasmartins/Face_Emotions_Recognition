import numpy as np
import scipy.io as scp
import os 
from PIL import Image 

data_dic ={"X":[],"y":[]}
    
# write angry pictures
entries = os.listdir('./images/train/angry')

cnt = 1
for image in entries:
    if cnt>1000:
        break
    image = Image.open('./images/train/angry/' + image).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([0])
    cnt+=1

# write disgust pictures
entries = os.listdir('./images/train/disgust')/255

cnt = 1
for image in entries:
    if cnt>1000:
        cnt=1
        break
    image = Image.open('./images/train/disgust/' + image).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([1])
    cnt+=1

# write fear pictures
entries = os.listdir('./images/train/fear')

cnt = 1
for image in entries:
    if cnt>1000:
        cnt=1
        break
    image = Image.open('./images/train/fear/' + image).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([2])
    cnt+=1

# write happy pictures
entries = os.listdir('./images/train/happy')

cnt = 1
for image in entries:
    if cnt>1000:
        cnt=1
        break
    image = Image.open('./images/train/happy/' + image).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([3])
    cnt+=1

# write neutral pictures
entries = os.listdir('./images/train/neutral')

cnt = 1
for image in entries:
    if cnt>1000:
        cnt=1
        break
    image = Image.open('./images/train/neutral/' + image).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([4])
    cnt+=1

# write sad pictures
entries = os.listdir('./images/train/sad')

cnt = 1
for image in entries:
    if cnt>1000:
        cnt=1
        break
    image = Image.open('./images/train/sad/' + image).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([5])
    cnt+=1

# write surprise pictures
entries = os.listdir('./images/train/surprise')

cnt = 1
for image in entries:
    if cnt>1000:
        cnt=1
        break
    image = Image.open('./images/train/surprise/' + image).convert('L')
    image = np.array(image)
    image = image.reshape(image.shape[0]**2)/255
    data_dic["X"].append(image)
    data_dic["y"].append([6])
    cnt+=1


scp.savemat('training_data.mat', data_dic)
