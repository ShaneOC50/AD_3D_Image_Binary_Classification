import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import gif2numpy

############################################################
##                                                        ##
##          Generate AD+CN ADNI Subject Slices            ##
##                                                        ##
############################################################

# ADNI AD Subject ADNI_073_S_1207_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070731112801664_S26777_I63127
ad_adni_subj_file_path = '/home/shane/Thesis/git/Dataset/ADNI/073_S_1207/MPR__GradWarp__B1_Correction__N3__Scaled/2007-02-15_16_18_42.0/I63127/ADNI_073_S_1207_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070731112801664_S26777_I63127.nii'
# ADNI CN Subject ADNI_033_S_1016_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070306084833503_S21817_I42772
cn_adni_subj_file_path = '/home/shane/Thesis/git/Dataset/ADNI/033_S_1016/MPR__GradWarp__B1_Correction__N3__Scaled/2006-11-01_09_23_40.0/I42772/ADNI_033_S_1016_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070306084833503_S21817_I42772.nii'

ad_img = nib.load(ad_adni_subj_file_path)
ad_img_data = np.array(ad_img.dataobj).astype('float32')
print(ad_img_data.shape)

cn_img = nib.load(cn_adni_subj_file_path)
cn_img_data = np.array(cn_img.dataobj).astype('float32')
print(cn_img_data.shape)

fig, axs = plt.subplots(2,3)
fig.suptitle('ADNI CN and AD Subject 3D MRI Slice Views')
axs[0,0].imshow(cn_img_data[120,:,:], cmap='gray')
axs[0,0].set_title('Axial View')
axs[0,0].set(ylabel='CN Subject')

axs[0,1].imshow(cn_img_data[:,135,:], cmap='gray')
axs[0,1].set_title('Coronal View')

axs[0,2].imshow(cn_img_data[:,:,90], cmap='gray')
axs[0,2].set_title('Sagittal View')


axs[1,0].imshow(ad_img_data[98,:,:], cmap='gray')
axs[1,0].set(ylabel='AD Subject')

axs[1,1].imshow(ad_img_data[:,96,:], cmap='gray')

axs[1,2].imshow(ad_img_data[:,:,73], cmap='gray')

fig.tight_layout()

plt.savefig('/home/shane/Thesis/git/Paper_Images/adni_ad_cn_slices.png', bbox_inches="tight", pad_inches=0.15, transparent=False)


############################################################
##                                                        ##
##     Resized - Generate AD+CN ADNI Subject Slices       ##
##                                                        ##
############################################################

# ADNI AD Subject ADNI_073_S_1207_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070731112801664_S26777_I63127
ad_resized_adni_subj_file_path = '/home/shane/Thesis/git/Dataset/ADNI/processed_data/2_ADNI_073_S_1207_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070731112801664_S26777_I63127.npy'
# ADNI CN Subject ADNI_033_S_1016_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070306084833503_S21817_I42772
cn_resized_adni_subj_file_path = '/home/shane/Thesis/git/Dataset/ADNI/processed_data/0_ADNI_033_S_1016_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070306084833503_S21817_I42772.npy'

ad_resized_adni_vol = np.load(ad_resized_adni_subj_file_path,allow_pickle=True)[0]
cn_resized_adni_vol = np.load(cn_resized_adni_subj_file_path,allow_pickle=True)[0]

fig, axs = plt.subplots(2,3)
fig.suptitle('Resized ADNI CN and AD Subject 3D MRI Slice Views')
axs[0,0].imshow(cn_resized_adni_vol[45,:,:], cmap='gray')
axs[0,0].set_title('Axial View')
axs[0,0].set(ylabel='CN Subject')
axs[0,1].imshow(cn_resized_adni_vol[:,52,:], cmap='gray')
axs[0,1].set_title('Coronal View')
axs[0,2].imshow(cn_resized_adni_vol[:,:,35], cmap='gray')
axs[0,2].set_title('Sagittal View')

axs[1,0].imshow(ad_resized_adni_vol[48,:,:], cmap='gray')
axs[1,0].set(ylabel='CN Subject')
axs[1,1].imshow(ad_resized_adni_vol[:,48,:], cmap='gray')
axs[1,2].imshow(ad_resized_adni_vol[:,:,35], cmap='gray')
fig.tight_layout()

plt.savefig('/home/shane/Thesis/git/Paper_Images/resized_adni_ad_cn_slices.png', bbox_inches="tight", pad_inches=0.15, transparent=False)


############################################################
##                                                        ##
##              Image Augmentation Atrategies             ##
##                                                        ##
############################################################

# using the cn resized image and subject

cn_rotated_filepath = '/home/shane/Thesis/git/Dataset/ADNI/augmentation/rotation/0_ADNI_033_S_1016_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070306084833503_S21817_I42772.npy'
cn_zoom_filepath = '/home/shane/Thesis/git/Dataset/ADNI/augmentation/zoom/0_ADNI_033_S_1016_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070306084833503_S21817_I42772.npy'
cn_shift_filepath = '/home/shane/Thesis/git/Dataset/ADNI/augmentation/shift/0_ADNI_033_S_1016_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070306084833503_S21817_I42772.npy'
cn_all_filepath = '/home/shane/Thesis/git/Dataset/ADNI/augmentation/all/0_ADNI_033_S_1016_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070306084833503_S21817_I42772.npy'
cn_original_vol = cn_resized_adni_vol

cn_rotated_adni_vol = np.load(cn_rotated_filepath,allow_pickle=True)[0]
cn_zoom_adni_vol = np.load(cn_zoom_filepath,allow_pickle=True)[0]
ad_shift_adni_vol = np.load(cn_shift_filepath,allow_pickle=True)[0]
cn_all_adni_vol = np.load(cn_all_filepath,allow_pickle=True)[0]

fig, axs = plt.subplots(2,3)
fig.suptitle('Image Augmentation 3D MRI Slice Views')
axs[0,0].imshow(cn_zoom_adni_vol[45,:,:], cmap='gray')
axs[0,0].set_title('Axial View')
axs[0,0].set(ylabel='Zoom')
axs[0,1].imshow(cn_zoom_adni_vol[:,52,:], cmap='gray')
axs[0,1].set_title('Coronal View')
axs[0,2].imshow(cn_zoom_adni_vol[:,:,35], cmap='gray')
axs[0,2].set_title('Sagittal View')

axs[1,0].imshow(ad_shift_adni_vol[48,:,:], cmap='gray')
axs[1,0].set(ylabel='Shift')
axs[1,1].imshow(ad_shift_adni_vol[:,48,:], cmap='gray')
axs[1,2].imshow(ad_shift_adni_vol[:,:,35], cmap='gray')

fig.tight_layout()

plt.savefig('/home/shane/Thesis/git/Paper_Images/augmented_img_slices_top.png', bbox_inches="tight", pad_inches=0.15, transparent=False)


fig, axs = plt.subplots(2,3)
fig.suptitle('Resized ADNI CN and AD Subject 3D MRI Slice Views')

axs[0,0].imshow(cn_rotated_adni_vol[48,:,:], cmap='gray')
axs[0,0].set(ylabel='Rotate')
axs[0,0].axis('off')
axs[0,0].set_title('Axial View')

axs[0,1].imshow(cn_rotated_adni_vol[:,48,:], cmap='gray')
axs[0,1].axis('off')

axs[0,1].set_title('Coronal View')

axs[0,2].imshow(cn_rotated_adni_vol[:,:,35], cmap='gray')
axs[0,2].axis('off')
axs[0,2].set_title('Sagittal View')


axs[1,0].imshow(cn_all_adni_vol[48,:,:], cmap='gray')
axs[1,0].set(ylabel='All')
axs[1,0].axis('off')
axs[1,1].imshow(cn_all_adni_vol[:,48,:], cmap='gray')
axs[1,1].axis('off')
axs[1,2].imshow(cn_all_adni_vol[:,:,35], cmap='gray')
axs[1,2].axis('off')

# axs[4,0].imshow(cn_all_adni_vol[48,:,:], cmap='gray')
# axs[4,0].set(ylabel='All')
# axs[4,1].imshow(cn_all_adni_vol[:,48,:], cmap='gray')
# axs[4,2].imshow(cn_all_adni_vol[:,:,35], cmap='gray')
# for a in fig:
#     a.set_xticklabels([])
#     a.set_yticklabels([])

# plt.subplots_adjust(wspace=0, hspace=0)
fig.tight_layout()

plt.savefig('/home/shane/Thesis/git/Paper_Images/augmented_img_slices_bottom.png', bbox_inches="tight", pad_inches=0.15, transparent=False)

# Combined the above two figures in powerpoint to make 1 image


############################################################
##                                                        ##
##     Resized - Generate AD+CN OASIS Subject Slices      ##
##                                                        ##
############################################################


# OASIS AD Subject ADNI_073_S_1207_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070731112801664_S26777_I63127
ad_resized_oasis_subj_file_path = '/home/shane/Thesis/git/Dataset/OASIS/processed_data/2_OAS1_0028_MR1_mpr_n4_anon_111_t88_gfc.npy'
# OASIS CN Subject ADNI_033_S_1016_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070306084833503_S21817_I42772
cn_resized_oasis_subj_file_path = '/home/shane/Thesis/git/Dataset/OASIS/processed_data/0_OAS1_0001_MR1_mpr_n4_anon_111_t88_gfc.npy'

ad_resized_oasis_vol = np.load(ad_resized_oasis_subj_file_path,allow_pickle=True)[0]
cn_resized_oasis_vol = np.load(cn_resized_oasis_subj_file_path,allow_pickle=True)[0]

fig, axs = plt.subplots(2,3)
fig.suptitle('Resized OASIS CN and AD Subject MRI 3D Slice Views')
axs[0,0].imshow(cn_resized_oasis_vol[45,:,:], cmap='gray')
axs[0,0].set_title('Axial View')
axs[0,0].set(ylabel='CN Subject')
axs[0,1].imshow(cn_resized_oasis_vol[:,52,:], cmap='gray')
axs[0,1].set_title('Coronal View')
axs[0,2].imshow(cn_resized_oasis_vol[:,:,35], cmap='gray')
axs[0,2].set_title('Sagittal View')

axs[1,0].imshow(ad_resized_oasis_vol[48,:,:], cmap='gray')
axs[1,0].set(ylabel='CN Subject')
axs[1,1].imshow(ad_resized_oasis_vol[:,48,:], cmap='gray')
axs[1,2].imshow(ad_resized_oasis_vol[:,:,35], cmap='gray')
fig.tight_layout()

plt.savefig('/home/shane/Thesis/git/Paper_Images/resized_oasis_ad_cn_slices.png', bbox_inches="tight", pad_inches=0.15, transparent=False)


oasis_subj_axial_filepath = '/home/shane/Thesis/OAS1_0028_MR1_mpr_n4_anon_111_t88_gfc_tra_90.gif'
oasis_subj_coronal_filepath = '/home/shane/Thesis/OAS1_0028_MR1_mpr_n4_anon_111_t88_gfc_cor_110.gif'
oasis_subj_sagittal_filepath = '/home/shane/Thesis/OAS1_0028_MR1_mpr_n4_anon_111_t88_gfc_sag_95.gif'

# oasis_subj_axial_im = Image.open(oasis_subj_axial_filepath)
oasis_subj_axial_im,a,b = gif2numpy.convert(oasis_subj_axial_filepath)
oasis_subj_coronal_im, a, b = gif2numpy.convert(oasis_subj_coronal_filepath)
oasis_subj_sagittal_im, a, b = gif2numpy.convert(oasis_subj_sagittal_filepath)



fig, axs = plt.subplots(1,3)
fig.suptitle('OASIS 3D MRI Slice Views')
axs[0].imshow(oasis_subj_axial_im[0], cmap='gray')
axs[0].set_title('Axial View')
axs[0].axis('off')
axs[1].imshow(oasis_subj_coronal_im[0], cmap='gray')
axs[1].set_title('Coronal View')
axs[1].axis('off')
axs[2].imshow(oasis_subj_sagittal_im[0], cmap='gray')
axs[2].set_title('Sagittal View')
axs[2].axis('off')

#fig.tight_layout()

plt.savefig('/home/shane/Thesis/git/Paper_Images/oasis_slices.png', bbox_inches="tight", pad_inches=0.15, transparent=False)


############################################################
##                                                        ##
##      Resized - Generate PET ADNI Subject Slices        ##
##                                                        ##
############################################################

adni_pet_filepath = '/home/shane/Thesis/git/Dataset/PET/processed_data/0_002_S_4213.npy'
adni_pet_vol = np.load(adni_pet_filepath,allow_pickle=True)[0]


fig, axs = plt.subplots(1,3)
fig.suptitle('ADNI PET 3D MRI Slice Views')
axs[0].imshow(adni_pet_vol[:,:,35], cmap='gray')
axs[0].set_title('Axial View')
axs[0].axis('off')
axs[1].imshow(np.rot90(adni_pet_vol[45,:,:]), cmap='gray')
axs[1].set_title('Coronal View')
axs[1].axis('off')
axs[2].imshow(np.rot90(adni_pet_vol[:,52,:]), cmap='gray')
axs[2].set_title('Sagittal View')
axs[2].axis('off')

plt.savefig('/home/shane/Thesis/git/Paper_Images/pet_slices.png', bbox_inches="tight", pad_inches=0.15, transparent=False)
