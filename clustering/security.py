# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd

X = pd.read_csv('../Data_FCDS_hashed/ent_social_security.csv',  usecols=['entname','unpaidsocialins_so110','unpaidsocialins_so210','unpaidsocialins_so310','unpaidsocialins_so410','unpaidsocialins_so510'])  # 读取训练数据
Y = X.dropna(axis=0)
data=Y[['unpaidsocialins_so110','unpaidsocialins_so210','unpaidsocialins_so310','unpaidsocialins_so410','unpaidsocialins_so510']]
clf = MiniBatchKMeans(n_clusters=2,init='k-means++',batch_size=100000)
clf.fit(data)
pre_clu = clf.labels_
Y['securitylabel'] = pre_clu
Y.to_csv("../clusteringResult/security.csv")