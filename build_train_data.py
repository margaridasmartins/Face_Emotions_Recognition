import numpy as np
import scipy.io as scp
import os 
from PIL import Image 

subsets = {
    'training': {
        'dir': './images/train/',
        'start': 0,
        'samples': 1000,
        'output': 'training_data'
    },
    'dev': {
        'dir': './images/test/',
        'start': 200,
        'samples': 200,
        'output': 'dev_data'
    },
    'test': {
        'dir': './images/test/',
        'start': 0,
        'samples': 200,
        'output': 'test_data'
    }
}

emotionsSet = [
    ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise'],
    ['disgust', 'surprise'],
    ['disgust', 'angry'],
    ['fear', 'angry'],
    ['happy', 'sad'],
    ['fear', 'angry', 'surprise'],
    ['fear', 'neutral', 'happy']
]

# Foreach emotion set
for emotions in emotionsSet:
    print("Emotion set",emotions)

    # Foreach subset 
    for subset, subsetinfo in subsets.items():
        data_dic ={"X":[],"y":[]}

        print("Subset", subset)
        i = 0

        # Foreach emotion
        for e in emotions:
            dir = subsetinfo['dir'] + e + '/'
            # For disgust on dev, get from train
            if e=='disgust' and subset=='dev':
                dir = './images/train/disgust/'
            entries = os.listdir(dir)
            cnt = 1
            print(i, e, end="\t\t\t")

            for image in entries[subsetinfo['start']::]:
                if cnt>subsetinfo['samples']:
                    break
                image = Image.open(dir + image).convert('L')
                image = np.array(image)
                image = image.reshape(image.shape[0]**2)/255
                data_dic["X"].append(image)
                data_dic["y"].append([i])
                cnt+=1
            
            print(f"Got {cnt-1} images!")
            i += 1    
        
        filename = subsetinfo['output'] + '_' + '_'.join(emotions) + '.mat'
        scp.savemat(filename, data_dic)
        print(f"Saved at {filename}\n")
    print()
    

