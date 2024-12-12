# training_and_evaluation performs the model training and tests it on the test dataset.
# NECESSARY PARAMETERS: data_path, nexp, augmentation, ndataset, n_conv_features, saver_path

# Parameters to set up:
#- data_path is the path to the folder containing the ADNI data: must to be a string
#- saver_path is the path to the folder in which the model and the results will be saved: must to be a string
#- nexp is the number of experiment performing model classification: must to be an integer
#- augmentation is the type augmented data to use in the model tranining: must be one of the following strings
#  "0" corresponds to non-augmented data,
#  "1" corresponds to zoom,
#  "2" corresponds to shift,
#  "3" corresponds to rotation,
#  "123" applies separately zoom, shift, and rotation,
#  "4" applied all transformations (zoom, shift,rotation) simultaneously.
#  "5" applies the "123" augmentation but creates X sets defined by ndataset.
#- ndataset sets how many augmented datasets have to be used: it must be an integer
#  it must be set to 1 for strategy A and B, whereas it has to be fixed at 3 for strategy C.
#  When augmentation = 5 it defines what size of the image augmentation saturation test dataset to use.
#- n_conv is the number of convolutional layers


# Set parameters for training and testing:
augmentation="123"    # Options: 0, 1, 2, 3, 123, 4, 5
ndataset=1            # This should be 1 unless using augmentation 4 or 5.
n_conv=8              # This defines the number of convolutional layers in the model. Best performance was found with 8.
epochs=300            # best performance uses 300 epochs with no early-stopping. Early-stopping is configurable in the training_and_evaluation.py file.
learning_rate=0.001   # Best performance was found using an initial learning rate of 0.001 for all trainable parameters in the model.
batch_size=32         # Best performance was using batch size of 32. Can be increased (memory allowing) to train models faster.
test_percentage=0.10  # This defines the train/val/test split to be 80/10/10. For very unbalanced datasets, use 0.15 as the value for a 70/15/15 split.\
# the following parameter defines the path to the weights that should be loaded and used as the initial weights by the model instead of randomly assigning them.
# By default this value is false so weights are randomly initialized.
transfer_learning_weights=False

frozen_layers=0       # When 0 Don't freeze any layers. When negative, freezes layers closer to the fully connected layer. When positive freezes layers starting at input layer.
# data_path defines where the folder that the processed and augmented image folders are stored in and to be used by the model.
data_path='/home/shane/Thesis/git/Dataset/ADNI/'
# saver_path defines where the logs, results, and model weights will be saved off at.
saver_path='/home/shane/Thesis/git/ADNI_Results/strategy_b_aug/'

# Run training and testing:
for nexp in {1..10} # 10 experiments can be used to evaluate model stability and robustness.
do
  echo "Experiment" $nexp ": ADNI AD/CN binary classification - saved at: " $saver_path
  python training_and_evaluation.py $data_path $nexp $augmentation $ndataset $n_conv $saver_path $epochs $learning_rate $batch_size $best_oasis_weights $test_percentage $frozen_layers
done