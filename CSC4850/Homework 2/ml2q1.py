from Bio import SeqIO
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

file = open("HW2.fas")
data = file.readlines()
names = []
seqs = []
for ind in range(len(data)):
    if ind%2 == 0:
        names.append(data[ind][1:-1])
    else:
        seqs.append(data[ind][:-1])
def hamming_distance(s1, s2):
    res = 0
    for ind in range(len(s1)):
        if s1[ind] != s2[ind]:
            res +=1
    return res
def get_hamming_distance(elems):
    res = []
    for s1 in elems:
        tmp = []
        for s2 in elems:
            tmp.append(hamming_distance(s1, s2))
        res.append(tmp)
    return np.array(res)
all_dists = get_hamming_distance(seqs)
mds = MDS(random_state=0, dissimilarity='precomputed')
mds_matrix = mds.fit_transform(all_dists)
plt.figure(figsize = (3,3))
plt.scatter(mds_matrix[:,0], mds_matrix[:,1])
plt.show()
model = KMeans(n_clusters=8).fit(mds_matrix)
plt.figure(figsize=(5,5))
plt.scatter(mds_matrix[:,0], mds_matrix[:,1], c = model.labels_.astype(float))
plt.show()
