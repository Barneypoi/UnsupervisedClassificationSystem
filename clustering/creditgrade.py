# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

A = pd.read_csv('../Data_FCDS_hashed/jn_credit_info.csv',  usecols=['entname','credit_grade'])
Y = A.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=2,init='k-means++',batch_size=1000)
clf.fit(Y[['credit_grade']])
pre_clu = clf.labels_
Y['credit_gradelabel'] = pre_clu
Y.to_csv("../clusteringResult/creditgrade.csv")