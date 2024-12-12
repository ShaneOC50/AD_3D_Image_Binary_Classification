""""""
import os
import numpy as np
from glob import glob as gg
import pandas as pd
import pydicom as dicom

data_path = '/home/shane/Thesis/git/Dataset/PET/'
study_folders = ['ADNI1/','ADNI2/','ADNI3/']

multi_class = "True"

print(data_path)
print(f'Multi Class = {multi_class}')

saver_path = data_path + 'dataset/'
if not os.path.exists(saver_path):
    os.makedirs(saver_path)

label_dic = {'CN': 0, 'MCI': 1, 'AD': 2}

n_CN = 0
n_AD = 0
n_MCI = 0
for study in study_folders:

    full_path = data_path + study
    csv_path = f'{full_path}PET_{study.strip("/")}_7_18_2024.csv'
    mri_table = pd.read_csv(csv_path)
    subjects = mri_table['Subject']
    subject_groups = mri_table['Group']

    subfolders = [ f.path for f in os.scandir(full_path) if f.is_dir() ]

    subject_dict = {}

    for subfolder in subfolders:
        subject = subfolder.split('/')[-1]
        subject_dict[subject] = {}
        subject_dict[subject]["file_paths"]=[]
        subject_dict[subject]["img3d"] = np.zeros([160,160,96])
        for path in gg(f'{subfolder}/**/*.dcm',
                                recursive = True):
            subject_dict[subject]["file_paths"].append(path)
            # fill 3D array with the images from the files
            ds = dicom.dcmread(path)
            try:
                index = int(path.split("_")[-3])-1
            except:
                index = int(path.split("_")[-1].split(".")[0])-1
            img2d = ds.pixel_array
            subject_dict[subject]["img3d"][:, :, index] = img2d
        data = np.array(subject_dict[subject]["img3d"]).astype('float32')
        correspondence = np.where(np.array(subjects) == subject)[0]
        label = label_dic[subject_groups[correspondence[0]]]
        saver_name = str(label) + '_' + subject
        np.save(saver_path + saver_name, (data, label))
