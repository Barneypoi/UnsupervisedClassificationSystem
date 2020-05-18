# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

A = pd.read_csv('../Data_FCDS_hashed/intangible_patent.csv',  usecols=['entname','ipat_num'])
Y = A.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=3,init='k-means++',batch_size=1000)
clf.fit(Y[['ipat_num']])
pre_clu = clf.labels_
Y['ipat_numlabel'] = pre_clu
Y.to_csv("../clusteringResult/patentnum.csv")