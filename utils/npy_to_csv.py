#Don't Forgot to add FIRST LINE!!!!
import numpy as np

output = np.load('output_12_1.npy')

index = np.arange(1,output.shape[0]+1)
index = index[:,np.newaxis]

output = np.concatenate([index, output], 1)

np.savetxt('output_12_1.csv', output, fmt="%d,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f", delimiter=',')
