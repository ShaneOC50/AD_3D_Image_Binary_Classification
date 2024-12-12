import os
import sys
import csv

data_path = str(sys.argv[1])
masked = int(sys.argv[2])

files = []
print(masked)

if masked == 0:
    print("No mask used")
    for dirpath, dirnames, filenames in os.walk(data_path):
        for filename in [f for f in filenames if f.endswith("111_t88_gfc.img")]:
            files.append([os.path.join(dirpath, filename)])

    print(len(files))

    with open('OASIS_img_files_noMask.csv','w') as newFile:
        writer = csv.writer(newFile)
        writer.writerow(['Paths'])
        for file in files:
            writer.writerow(file)
else:
    print("Using Masked Images")
    for dirpath, dirnames, filenames in os.walk(data_path):
        for filename in [f for f in filenames if f.endswith("111_t88_masked_gfc.img")]:
            files.append([os.path.join(dirpath, filename)])

    print(len(files))

    with open('OASIS_img_files_Masked.csv','w') as newFile:
        writer = csv.writer(newFile)
        writer.writerow(['Paths'])
        for file in files:
            writer.writerow(file)