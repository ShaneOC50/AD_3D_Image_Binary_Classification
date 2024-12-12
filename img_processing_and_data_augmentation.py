import os
import numpy as np
import sys
from glob import glob as gg
from img_processing_functions import *
data_path = str(sys.argv[1])
testing_aug_limit = int(sys.argv[2])

##
# ###################
#     UTILITIES     #
# ###################

print(np.version.version)

def img_processing(data, param, zoom=False, shift=False, rotation=False):
    """
    :param data: file name
    :param param: class function containing the parameters of the affine transformations
    :param zoom: set it to True to perform image zoom
    :param shift: set it to True to perform image shift
    :param rotation: set it to True to perform image rotation
    :return: transformed image and the associated label
    """
    Ndim = len(param.smallest_img_size)
    #final_dim = [int(d / int(1/param.scaling)) for d in param.smallest_img_size]
    final_dim = [96, 96, 73]
    input_image, label = np.load(data, allow_pickle=True)
    if zoom:
        input_image = random_zoom(input_image, min_percentage=param.z_min, max_percentage=param.z_max)
    if shift:
        input_image = random_shift(input_image)
    if rotation:
        input_image = random_3Drotation(input_image, min_angle=param.min_angle, max_angle=param.max_angle)
    input_image = resize_data_volume_by_scale(input_image, scale=param.scaling)
    new_scaling = [final_dim[i]/input_image.shape[i] for i in range(Ndim)]
    final_image = resize_data_volume_by_scale(input_image, scale=new_scaling)
    return final_image, label


##
# ###################
#  Set Parameters   #
# ###################

class Parameter(object):
    def __init__(self):
        self.smallest_img_size = [160, 160, 96]  # dimension of the smallest image
        self.scaling = 0.5  # scaling to apply to all images
        # Zoom parameters:
        self.z_min = 0.8  # minimum percentage
        self.z_max = 1.2  # maximum percentage
        # Rotation parameters:
        self.min_angle = -5  # minimum angle rotation
        self.max_angle = 5   # maximum angle rotation


param = Parameter()
#if "OASIS" in data_path:
#    param.smallest_img_size = [176, 208, 176]

# Define saving folders:
for folder in ['processed_data/', 'augmentation/']:
    if not os.path.exists(data_path + folder):
        os.makedirs(data_path + folder)

for subfolder in ['zoom/', 'shift/', 'rotation/', 'all', 'all2', 'all3','max_data']:
    if not os.path.exists(data_path + 'augmentation/' + subfolder):
        os.makedirs(data_path + 'augmentation/' + subfolder)

# Load npy imaging data: 0 and 2 corresponds to control and AD subjects
if ("ADNI" in data_path) or ("OASIS" in data_path) or ("PET" in data_path):
    print("Using ADNI or OASIS only datasets")
    files = gg(data_path + 'dataset/0*.npy') + gg(data_path + 'dataset/2*.npy')
else:
    files = gg(data_path + 'ADNI/dataset/0*.npy') + gg(data_path + 'ADNI/dataset/2*.npy') + gg(data_path + 'OASIS/dataset/0*.npy') + gg(data_path + 'OASIS/dataset/2*.npy')
    print("Using combined datasets")

print(f'The total number of .npy files found is : {len(files)}!\n')

# Start pre-processing and data augmentation:
for f in files:
    if testing_aug_limit == 0:
        name = os.path.basename(f).split('.npy')[0]
        # Processing
        processed_data = img_processing(f, param)
        np.save(data_path + 'processed_data/' + name + '.npy', processed_data)
        # Data Augmentation: transformation are applied separately
        processed_data = img_processing(f, param, zoom=True)
        np.save(data_path + 'augmentation/zoom/' + name + '.npy', processed_data)
        processed_data = img_processing(f, param, shift=True)
        np.save(data_path + 'augmentation/shift/' + name + '.npy', processed_data)
        processed_data = img_processing(f, param, rotation=True)
        np.save(data_path + 'augmentation/rotation/' + name + '.npy', processed_data)
        # Data Augmentation: transformation are applied simultaneously
        processed_data = img_processing(f, param, zoom=True, shift=True, rotation=True)
        np.save(data_path + 'augmentation/all/' + name + '.npy', processed_data)
        processed_data = img_processing(f, param, zoom=True, shift=True, rotation=True)
        np.save(data_path + 'augmentation/all2/' + name + '.npy', processed_data)
        processed_data = img_processing(f, param, zoom=True, shift=True, rotation=True)
        np.save(data_path + 'augmentation/all3/' + name + '.npy', processed_data)
    else:
        if f == files[0]:
            print(f'Creating {3*len(files)*len(list(range(testing_aug_limit)))} new augmentated files in {data_path}augmentation/max_data/ folder!\n')
        for iter in range(testing_aug_limit):

            name = f'{os.path.basename(f).split(".npy")[0]}_batch_{iter}'

            # # Processing
            # processed_data = img_processing(f, param)
            # np.save(data_path + 'processed_data/' + name + '.npy', processed_data)

            processed_data = img_processing(f, param, zoom=True)
            np.save(data_path + 'augmentation/max_data/' + name + '_zoom.npy', processed_data)
            processed_data = img_processing(f, param, shift=True)
            np.save(data_path + 'augmentation/max_data/' + name + '_shift.npy', processed_data)
            processed_data = img_processing(f, param, rotation=True)
            np.save(data_path + 'augmentation/max_data/' + name + '_rotat.npy', processed_data)

