# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

X = pd.read_csv('../Data_FCDS_hashed/product_checkinfo_connect.csv',  usecols=['entname','passpercent'])  # 读取训练数据
Y = X.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=3,init='k-means++',batch_size=1000)
clf.fit(Y[['passpercent']])
pre_clu = clf.labels_
Y['passpercentlabel'] = pre_clu
Y.to_csv("../clusteringResult/quality.csv")