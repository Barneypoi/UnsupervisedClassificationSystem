# coding:utf-8
from sklearn import preprocessing
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

X = pd.read_csv('../Data_FCDS_hashed/ent_contribution.csv',  usecols=['entname','subconam','conprop'])  # 读取训练数据
Y = X.dropna(axis=0)
data=Y[['subconam','conprop']]
data=preprocessing.scale(data)
clf = MiniBatchKMeans(n_clusters=3,init='k-means++')
clf.fit(data)
pre_clu = clf.labels_
Y['contributionlabel'] = pre_clu
Y.to_csv("../clusteringResult/contribution.csv")