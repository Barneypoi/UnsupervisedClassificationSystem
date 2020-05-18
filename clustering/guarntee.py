# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

X = pd.read_csv('../Data_FCDS_hashed/ent_guarantee.csv',  usecols=['entname','priclasecam'])  # 读取训练数据
Y = X.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=2,init='k-means++')
clf.fit(Y[['priclasecam']])
pre_clu = clf.labels_
Y['priclasecamlabel'] = pre_clu
Y.to_csv("../clusteringResult/guarantee.csv")