import numpy as np
import scipy.io as scp
import os 
from PIL import Image 

subsets = {
    'test': {
        'dir': './datasets/images/goncalo_catalog/processed/',
        'start': 0,
        'samples': 200,
        'folder': './datasets/goncalo_catalog'
    }
}

# Create folders if they dont exist
for s in subsets.values():
    if not os.path.exists(s['folder']):
        os.makedirs(s['folder'])

emotionsSet = [
    ['happy', 'neutral']
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
        
        filename =  subsetinfo['folder'] +'/' + '_'.join(emotions) + '.mat'
        scp.savemat(filename, data_dic)
        print(f"Saved at {filename}\n")
        print("X", len(data_dic["X"]))
        print("y", len(data_dic["y"]))
        print("\n\n")
        
    print()
    

