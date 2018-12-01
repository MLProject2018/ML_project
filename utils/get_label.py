'''
@file  : get_label.py
@brief : get label from split files and then stored with npy file
@author: Lee
@date  : 12/1/2018
@history:
'''

import csv
import numpy as np

'''
@input : file(a str for file path); l(a list will be stored to the file)
@output: None
@brief: file has already been opened
@history: it is not used in this file

'''

'''
@brief: main function process
'''

base_name = '../data/split_'
suffix_name = '.csv'
label_list_save = []
f_label = file('../data/label.npy', 'wb')
pre_fileid = 0
for file_num in xrange(1, 10):
    filename = base_name + str(file_num) + suffix_name  # a better expression
    with open(filename) as f:
        print('\n\n handing %s' % filename)
        reader = csv.reader(f)
        try:
            for row in reader:
                # get fileid and tid
                fileid = int(row[0])
                label = int(row[1])

                # save one label for each kind of fileid
                if pre_fileid != fileid:
                    label_list_save.append(label)
                    print(fileid, label)

                pre_fileid = fileid  # update pre_fileid
        except:
            print('Error')
            exit(0)

# save label information to npy file
np.save(f_label, label_list_save)
print('total label: %d' % len(label_list_save))
f_label.close()
