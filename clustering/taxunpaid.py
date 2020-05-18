# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

A = pd.read_csv('../Data_FCDS_hashed/business_risk_taxunpaid.csv',  usecols=['entname','taxunpaidnum'])
Y = A.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=4,init='k-means++',batch_size=1000)
clf.fit(Y[['taxunpaidnum']])
pre_clu = clf.labels_
Y['taxunpaidnumlabel'] = pre_clu
Y.to_csv("../clusteringResult/taxunpaid.csv")