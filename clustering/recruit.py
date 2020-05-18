# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

A = pd.read_csv('../Data_FCDS_hashed/recruit.csv',  usecols=['entname','recruitnum'])
Y = A.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=4,init='k-means++',batch_size=1000)
clf.fit(Y[['recruitnum']])
pre_clu = clf.labels_
Y['recruitnumlabel'] = pre_clu
Y.to_csv("../clusteringResult/recruit.csv")