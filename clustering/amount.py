# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

X = pd.read_csv('../Data_FCDS_hashed/justice_enforced.csv',  usecols=['entname','enforce_amount'])  # 读取训练数据
Y = X.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=3,init='k-means++')
clf.fit(Y[['enforce_amount']])
pre_clu = clf.labels_
Y['amountlabel'] = pre_clu
Y.to_csv("../clusteringResult/amount.csv")