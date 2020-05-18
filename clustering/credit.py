# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

A = pd.read_csv('../Data_FCDS_hashed/justice_credit.csv',  usecols=['entname','is_justice_credit'])
Y = A.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=3,init='k-means++',batch_size=1000)
clf.fit(Y[['is_justice_credit']])
pre_clu = clf.labels_
Y['is_justice_creditlabel'] = pre_clu
Y.to_csv("../clusteringResult/credit.csv")