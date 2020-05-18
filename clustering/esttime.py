# coding:utf-8
from sklearn.cluster import MiniBatchKMeans
import pandas as pd
X = pd.read_csv('../Data_FCDS_hashed/company_baseinfo.csv',  usecols=['entname','estdate'])  # 读取训练数据
Y = X.dropna(axis=0)
clf = MiniBatchKMeans(n_clusters=3,init='k-means++')
clf.fit(Y[['estdate']])
pre_clu = clf.labels_
Y['estdatelabel'] = pre_clu
Y.to_csv("../clusteringResult/estdate.csv")

