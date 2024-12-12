""""""
import os
import numpy as np
import nibabel as nib
from glob import glob as gg
import pandas as pd
import sys

data_path = str(sys.argv[1])
multi_class = str(sys.argv[2])

print(data_path)
print(f'Multi Class = {multi_class}')

saver_path = data_path + 'dataset/'
if not os.path.exists(saver_path):
    os.makedirs(saver_path)

#files = gg(data_path + '**/*Scaled_Br*.nii', recursive=True)

files = []
subj_list = []
for dirpath, dirnames, filenames in os.walk(data_path):
    for filename in [f for f in filenames if f.endswith(".nii")]:
        subject_name = "_".join(os.path.basename(filename).split('/')[-1].split("_")[1:4])
        if subject_name not in subj_list:
            subj_list.append(subject_name)
            files.append(os.path.join(dirpath, filename))

print(f'The total number of .nii files found is : {len(files)}!\n')

img = [nib.load(f) for f in files]

data = [np.array(i.dataobj).astype('float32') for i in img]

label_dic = {'CN': 0, 'MCI': 1, 'AD': 2}

n_CN = 0
n_AD = 0
n_MCI = 0
if "OASIS" in data_path:
    mri_table = pd.read_csv(data_path + 'oasis_cross-sectional.csv')

    subjects = mri_table['ID']
    subject_groups = mri_table['CDR']

    j = 0
    for name in files:
        subject_name = os.path.basename(name).split('_mpr_')[0]
        correspondence = np.where(np.array(subjects) == subject_name)[0]
        #print(f'Correspondence = {correspondence} AND File Name = {name}')
        cdr_score = subject_groups[correspondence[0]]
        if cdr_score > 0:
            label = label_dic['AD']
            n_AD += 1
        else:
            label = label_dic['CN']
            n_CN += 1
        saver_name = str(label) + '_' + name.split('/')[-1].split('.nii')[0]
        np.save(saver_path + saver_name, (data[j], label))
        j += 1
elif "PET_MRIs" in data_path:
    mri_table = pd.read_csv(data_path + 'Best_Chance_MRI_PET_8_05_2024.csv')

    subjects = mri_table['Subject']
    subject_groups = mri_table['Group']

    subj_list = []

    j = 0
    for name in files:
        subject_name = os.path.basename(name).split('ADNI_')[1].split('_MR')[0]
        correspondence = np.where(np.array(subjects) == subject_name)[0]
        #print(f'Correspondence = {correspondence} AND File Name = {name}')
        label = label_dic[subject_groups[correspondence[0]]]
        saver_name = str(label) + '_' + name.split('/')[-1].split('.nii')[0]
        np.save(saver_path + saver_name, (data[j], label))
        j += 1
    
    print(len(subj_list))

else:
    if multi_class:
        mri_table = pd.read_csv(data_path + 'Multiclass_Turrisi_3dCNN_2_27_2024.csv')
    else:    
        mri_table = pd.read_csv(data_path + 'Turrisi_3dCNN_2_27_2024.csv')

    subjects = mri_table['Subject']
    print(len(files))
    subject_groups = mri_table['Group']

    j = 0
    for name in files:
        subject_name = os.path.basename(name).split('ADNI_')[1].split('_MR')[0]
        correspondence = np.where(np.array(subjects) == subject_name)[0]
        #print(f'Correspondence = {correspondence} AND File Name = {name}')
        label = label_dic[subject_groups[correspondence[0]]]
        saver_name = str(label) + '_' + name.split('/')[-1].split('.nii')[0]
        np.save(saver_path + saver_name, (data[j], label))
        j += 1

# show the size of the images
all_possible_sizes = list(set(list([d.shape for d in data])))
n_sizes = len(all_possible_sizes)

sizes = [[] for i in range(n_sizes)]
for i in range(len(data)):
    s = data[i].shape
    for n in range(n_sizes):
        if s == all_possible_sizes[n]:
            sizes[n].append(i)

dim = [len(i) for i in sizes]

textfile = open(data_path + 'dataset_info.txt', 'w')

for i in range(n_sizes):
    print(str(dim[i]) + ' images have size ' + str(all_possible_sizes[i]))
    textfile.write(str(dim[i]) + ' images have size ' + str(all_possible_sizes[i]) + '\n')

textfile.write('\n')

textfile.write(f'The number of demented samples is {n_AD}')
textfile.write('\n')

textfile.write(f'The number of NON-demented samples is {n_CN}')
textfile.write('\n')
textfile.write('\n')

for i in range(n_sizes):
    textfile.write('List of subjects with MRI size equal to ' + str(all_possible_sizes[i]) + ': \n\n')
    for j in sizes[i]:
        textfile.write(files[j].split('/')[-1].split('.nii')[0] + '\n')
    textfile.write('\n')

''' 
Output:

81 images have size (256, 256, 170)
2 images have size (256, 256, 160)
271 images have size (256, 256, 166)
1 images have size (256, 256, 161)
1 images have size (256, 256, 162)
320 images have size (192, 192, 160)
1 images have size (256, 256, 146)
12 images have size (256, 256, 184)
119 images have size (256, 256, 180)

'''
