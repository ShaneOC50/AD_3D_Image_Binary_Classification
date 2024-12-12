# Run this script in the terminal using the command './image_preprocessing.sh'

# Define the path to the folder containing the raw images to be used.
data_path='/home/shane/Thesis/git/Dataset/ADNI/'

# When testing the affects of image augmentation, use this field to define how many augmented sets of each augmentation strategy B you would like to create. 
# By default this value should be 0 to create the augmented datasets for Strategies A, B, and C.
num_augmented_datasets=0

# multi_class is a flag that can be passed in to tell the python functions how many classes are going to be used.
# NOTE: The multi-class capabilities have not been fully developed as of 12/11/2024!!
multi_class=False

# This function will convert all Nifti file images in the data_path into numpy array object files.
python3 from_nii_to_npy.py $data_path $multi_class  # converts files from nii to numpy and creates a txt file containing images size information

python3 img_processing_and_data_augmentation.py $data_path $testing_aug_limit