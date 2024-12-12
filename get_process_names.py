import os

data_file = 'PATH TO ADNI SUBJECTS CSV FILE'

CN_scan_types = []
CN_subjects = []
AD_scan_types = []
AD_subjects = []

with open(data_file,'r') as txt:
    lines = txt.readlines()
    for idx,line in enumerate(lines):
        if (idx < 310):
            process = line.strip('\n').split('_')
            subj = "_".join(process[1:4])
            if not(subj in CN_subjects):
                CN_subjects.append(subj)
            for list_ind,section in enumerate(process):
                if list_ind > 5 and section.isnumeric():
                    if float(section) > 10:
                        end_ind = list_ind
                        process = "_".join(process[5:list_ind-1])
            if not(process in CN_scan_types):
                CN_scan_types.append(process)
        elif idx > 313:
            process = line.strip('\n').split('_')
            subj = "_".join(process[1:4])
            if not(subj in AD_subjects):
                AD_subjects.append(subj)
            for list_ind,section in enumerate(process):
                if list_ind > 5 and section.isnumeric():
                    if float(section) > 10:
                        end_ind = list_ind
                        process = "_".join(process[5:list_ind-1])
            if not(process in AD_scan_types):
                AD_scan_types.append(process)

CN_scan_types = CN_scan_types[2:]

print(sorted(CN_scan_types))
print(len(CN_scan_types))
print(sorted(CN_subjects))
print(len(CN_subjects))

print(sorted(AD_scan_types))
print(len(AD_scan_types))
print(sorted(AD_subjects))
print(len(AD_subjects))