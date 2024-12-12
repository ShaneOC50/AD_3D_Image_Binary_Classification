# AD Binary Classification

This code repository is used to generate and run an 8 layer convolutional neural network which is used for binary classification of Alzheimer's disease. There are bash scripts to perform the image preprocessing and generate augmented images. Another bash script is used to generate and run the model evaluation.

# Image Preprocessing Files
The following files are used to generate the numpy array files compatible with the model. For image preprocessing, use a python environment with the packages and versions in the image_processing_requirements.txt file.

## image_preprocessing.sh
This bash script is used to convcert Nifiti images into the numpy objects and then create the augmented images from the dataset. The two function calls in this script can be separated if desired.

## from_nii_to_npy.py
This is the first python function that is called by the image_preprocessing.py script and converts the Nifti images into the Numpy array object formatting that the model will require as an input.

## img_processing_and_data_augmentation.py
This is the second function that is called in the image_preprocessing.sh script. It is responsible for generating the augmented datasets and defining the transformations their parameters.

## img_processing_functions.py
This file contains the actual transformation function definitions used in img_processing_and_data_augmentation.py.

## convert_dcm2npy.py
This file can be used to convert all Dicom images in a folder into numpy arrays of the images.


# Model Executing Files
The following files are used to generate the model, train and test it. When executing these files use a python environment with the packages and versions in the model_evaluation_requirements.txt. The same python environment should be used for the Miscellaneous files as well. Note that some of the packages are only required when running on a CUDA device.

## run.sh
This is the bash script used to build and evaluate the model. It has multiple input parameters defined within the file. They are used to define hyperparameters of the model for testing, what the dataset in use is, the augmentation strategy to be used, if transfer learning is being used, what train/val/test split breakdown should be used, and what method of transfer learning will be used.

## training_and_evaluation.py
This file is called by the run.sh script. It is responsible for building, training, validating, and testing the model. It reports the results in log files saved off in the saver path defined in the run.sh script. The model is built and tested using methods in the cnn_utilities.py file.

## cnn_utilities.py
This file contains the building block methods for the model defined in the training_and_evaluation.py file.


# Miscellaneous Files

## find_all_img_files.py
This file can be called using a data path and mask flag to find all of the desired OASIS images in the data path.

## result_plots.py
This file can be used to generate box and whisker plots of the results from the folders created by model runs. The plots folder paths can be defined in the file as a list. Used when the number of experiments a model was run for is 10.

## new_test_result_plots.py
This script does essentially the same as above but should be used when the model was only tested for 5 experiments.

## get_process_names.py
This file can be used to define the ADNI image processing types that were used to be searched in the ADNI database as the image descriptions.

## image_viewing.py
This script contains code to generate views of the MRI or PET images being fed into the model by using of Matplotlib.