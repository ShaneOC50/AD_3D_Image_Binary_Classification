import numpy as np 
import matplotlib.pyplot as plt


paths = ['/home/shane/Thesis/git/PET_Results/']

for results_path in paths:
    print(results_path)
    max_error_val = results_path.split('/')[-2].split('_')[-1]

    #test_data_paths = ["epoch_250_LR001","epoch_250_LR0004","epoch_300_LR001","epoch_300_LR0004"]
    #test_data_paths = ["net_8CL_no_aug", "net_8CL_all_aug"]
    #test_data_paths = ["net_8CL_batch8","net_8CL_batch16","net_8CL_batch32","net_8CL_batch64"]
    test_data_paths = ["net8cl_all_aug","net8cl_all_aug_3_datasets","net8cl_no_aug","net8cl_separate_aug"]

    experiments = []
    test_result_dic = {}
    for test in test_data_paths:
        test_result_dic[test] = {"exp_fold_accuracies":[], "overall_exp_accuracies":[]}
        for i in range(1,6):
            experiments.append(test + "/Exp" + str(i))

    exp_accuracies = []
    for test in test_result_dic.keys():
        exp_accuracies = []
        for i in range(1,6):
            exp_log_path = results_path + test + "/Exp" + str(i) + "/logfile.txt"
            with open(exp_log_path, 'r') as logFile:
                lines = logFile.readlines()
                for line in lines:
                    if line.startswith("Testing accuracy: "):
                        exp_accuracies.append(float(line.split(": ")[-1].strip('\n')))
                    if "Weighted Testing accuracy: " in line:
                        test_result_dic[test]["overall_exp_accuracies"].append(float(line.split(": ")[-1].strip('\n')))
            test_result_dic[test]["exp_fold_accuracies"].append(exp_accuracies)

    # Create Box and Whisker Plots for Overall Test accuracies
    exp_fold_accuracies = []
    overall_exp_accuracies = []
    for test in test_result_dic.keys():
        overall_exp_accuracies.append(np.array(test_result_dic[test]["overall_exp_accuracies"]))
        print("The accuracy of "+test+" is "+str(np.round(100*np.mean(np.array(test_result_dic[test]["overall_exp_accuracies"])),2)) + " +/- "+str(np.round(100*np.std(np.array(test_result_dic[test]["overall_exp_accuracies"])),2)))

    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)

    meanpointprops = {"marker":'*',"markersize":20,"markeredgecolor":'black', "markerfacecolor":'red'}

    # Creating axes instance
    LABELS = test_result_dic.keys()
    bp = ax.boxplot(overall_exp_accuracies, patch_artist = True,
                    labels = LABELS, meanprops=meanpointprops, showmeans=True)

    colors = ['#0000FF', '#00FF00',
            '#FFFF00', '#BBBBBB']

    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color ='#8B008B',
                    linewidth = 1.5,
                    linestyle =":")

    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color ='#8B008B',
                linewidth = 2)

    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color ='pink', linewidth = 3)

    # changing style of fliers
    for flier in bp['fliers']:
        flier.set(marker ='D',
                color ='#e7298a',
                alpha = 0.5)

    # Adding title
    plt.title("Overall Strategy Accuracies across Tests")

    # Add y-axis label
    ax.set_ylabel('Accuracy')


    # Removing top axes and right axes
    # ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    plt.savefig(results_path+"output"+max_error_val+".jpg", bbox_inches="tight", pad_inches=0.15, transparent=False)