import csv
import numpy as np

with open('../data/api_list.txt') as f:
    l = eval(f.read())
print(len(l))

total = []

base_name = '../data/split_'
suffix_name = '.csv'
for file_id in range(1,10): # traverse all file
    filename = base_name + str(file_id) + suffix_name
    with open(filename, errors='ignore') as f:
        print('\n\n handling ', str(filename))
        reader = csv.reader(f)
        file_id = -1

        try:
            for row in reader:
                if file_id != int(row[0]): # new file_id
                    if file_id != -1: # first file_id in this split_*
                        total.append(np.array([api_vec])) # record previous file_id's api_vec
                    #print("Processing ", row[0])
                    api_vec = [0]*296 # create new api_vec
                    file_id = int(row[0])
                api = row[2]
                api_vec[l.index(api)] += 1
        except Exception as  e:
            print(e)
            input() # wait for command
        total.append(np.array([api_vec]))
        print(len(total))

res = np.concatenate(total, 0)
print(res.shape) # (13887,296)
np.save('../data/api_vec.npy', res)
