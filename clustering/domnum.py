# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

A = pd.read_csv('../Data_FCDS_hashed/web_record_info.csv',  usecols=['entname','idom_num'])
Y = A.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=3,init='k-means++',batch_size=1000)
clf.fit(Y[['idom_num']])
pre_clu = clf.labels_
Y['idom_numlabel'] = pre_clu
Y.to_csv("../clusteringResult/domnum.csv")