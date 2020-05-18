# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

A = pd.read_csv('../Data_FCDS_hashed/business_risk_rightpledge.csv',  usecols=['entname','pledgenum'])
Y = A.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=2,init='k-means++',batch_size=100)
clf.fit(Y[['pledgenum']])
pre_clu = clf.labels_
Y['pledgenumlabel'] = pre_clu
Y.to_csv("../clusteringResult/rightpledge.csv")