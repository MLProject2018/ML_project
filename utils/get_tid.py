'''
@file  : get_tid.py
@brief : get tid vecotr from split files and then stored with npy file
@author: Lee
@date  : 11/30/2018
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


def write_list_to_file(file, l):
    for e in l:
        file.write(str(e))
        file.write(' ')
    file.write('\n')


'''
@brief: main function process
'''
# filenames = ['../split_1.csv', '../split_2.csv', '../split_3.csv', '../split_4.csv',
#              '../split_5.csv', '../split_6.csv', '../split_7.csv', '../split_8.csv', '../split_9.csv']
base_name = '../split_'
suffix_name = '.csv'
for file_id in xrange(1, 10):
    filename = base_name + str(file_id) + suffix_name  # a better expression
    with open(filename) as f:
        print('\n\n handing %s' % filename)
        fileid_tid_dict = {}
        fileid_list_save = []
        tid_list_save = []
        pre_fileid = 0
        f_tid = file('../data/tidlist.npy', 'wb')
        f_fileid = file('../data/fileidlist.npy', 'wb')
        reader = csv.reader(f)
        try:
            tid_list = []
            for row in reader:
                # get file_id and tid
                fileid = int(row[0])
                tid = int(row[3])

                # statistics
                if fileid not in fileid_tid_dict.keys():  # add a new fileid
                    fileid_tid_dict[fileid] = [1]  # init tid number vector
                    tid_list = [tid]  # init tid record

                    fileid_list_save.append(fileid)
                    if pre_fileid:
                        tid_list_save.append(len(fileid_tid_dict[pre_fileid]))
                        print(pre_fileid, len(fileid_tid_dict[pre_fileid]))
                else:  # count tid's num of this fileid
                    if tid not in tid_list:  # repeat elem that we do not care
                        tid_list.append(tid)  # update tid list
                        fileid_tid_dict[fileid].append(1)  # add a new kind of tid
                    else:
                        fileid_tid_dict[fileid][-1] += 1  # update num of tid at the last elem
                pre_fileid = fileid

        except:
            print('Error')
        # save the last tid
        tid_list_save.append(len(fileid_tid_dict[pre_fileid]))

        # save tid information to npy file
        np.save(f_fileid, fileid_list_save)
        np.save(f_tid, tid_list_save)
        # print(pre_fileid, fileid_tid_dict[pre_fileid])
        print('total line: %d' % len(fileid_tid_dict.keys()))
        f_tid.close()
        f_fileid.close()
