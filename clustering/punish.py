# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

A = pd.read_csv('../Data_FCDS_hashed/punish.csv',  usecols=['entname','punish'])
Y = A.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=2,init='k-means++',batch_size=1000)
clf.fit(Y[['punish']])
pre_clu = clf.labels_
Y['punishlabel'] = pre_clu
Y.to_csv("../clusteringResult/punish.csv")