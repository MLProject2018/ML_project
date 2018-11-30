'''
@file  : test_read_tid.py
@brief : a test to load npy file
@author: Lee
@date  : 11/30/2018
@history:
'''

import numpy as np

f_fileid = np.load('../data/fileidlist.npy')
f_tid = np.load('../data/tidlist.npy')

for i in xrange(0, f_fileid.size):
    print(f_fileid[i], f_tid[i])
