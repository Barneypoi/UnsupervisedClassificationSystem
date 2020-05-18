# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

X = pd.read_csv('../Data_FCDS_hashed/ent_bid.csv',  usecols=['entname','bidnum'])  # 读取训练数据
Y = X.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=4,init='k-means++',batch_size=1000)
clf.fit(Y[['bidnum']])
pre_clu = clf.labels_
Y['bidnumlabel'] = pre_clu
Y.to_csv("../clusteringResult/bid.csv")