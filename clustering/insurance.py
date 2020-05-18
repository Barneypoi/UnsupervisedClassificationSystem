# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

X = pd.read_csv('../Data_FCDS_hashed/enterprise_insurance.csv',  usecols=['entname','cbrq'])  # 读取训练数据
Y = X.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=3,init='k-means++',batch_size=10000)
clf.fit(Y[['cbrq']])
pre_clu = clf.labels_
Y['cbrqlabel'] = pre_clu
Y.to_csv("../clusteringResult/insurance.csv")