# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

X = pd.read_csv('../Data_FCDS_hashed/ent_contribution_year.csv',  usecols=['entname','liacconam','lisubconam'])  # 读取训练数据
Y = X.dropna(axis=0)
data=Y[['liacconam','lisubconam']]
clf = MiniBatchKMeans(n_clusters=3,init='k-means++',batch_size=1000)
clf.fit(data)
pre_clu = clf.labels_
Y['yearlabel'] = pre_clu
Y.to_csv("../clusteringResult/year.csv")