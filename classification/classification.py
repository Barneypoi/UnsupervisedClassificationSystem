# coding: utf-8
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np


def newalttime(input):
    X = pd.read_csv('../clusteringResult/alttime.csv',  usecols=['alttime','alttimelabel'])  # 读取训练数据
    data_train=X[['alttime']].head(10000).values
    label_train=X[['alttimelabel']].head(10000).values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result


def newestdate(input):
    X = pd.read_csv('../clusteringResult/estdate.csv',  usecols=['estdate','estdatelabel'])  # 读取训练数据
    data_train=X[['estdate']].values
    label_train=X[['estdatelabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result


def newregcap(input):
    X = pd.read_csv('../clusteringResult/regcap.csv',  usecols=['regcap','regcaplabel'])  # 读取训练数据
    data_train=X[['regcap']].head(10000).values
    label_train=X[['regcaplabel']].head(10000).values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newshopnum(input):
    X = pd.read_csv('../clusteringResult/shopnum.csv',  usecols=['shopnum','shopnumlabel'])  # 读取训练数据
    data_train=X[['shopnum']].values
    label_train=X[['shopnumlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newbranchnum(input):
    X = pd.read_csv('../clusteringResult/branchnum.csv',  usecols=['branchnum','branchnumlabel'])  # 读取训练数据
    data_train=X[['branchnum']].values
    label_train=X[['branchnumlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newcontribution(input1,input2):
    X = pd.read_csv('../clusteringResult/contribution.csv',  usecols=['subconam','conprop','contributionlabel'])  # 读取训练数据
    data_train=X[['subconam','conprop']].head(10000).values
    label_train=X[['contributionlabel']].head(10000).values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input1,input2]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newyear(input1,input2):
    X = pd.read_csv('../clusteringResult/year.csv',  usecols=['yearlabel','liacconam','lisubconam'])  # 读取训练数据
    data_train=X[['liacconam','lisubconam']].head(10000).values
    label_train=X[['yearlabel']].head(10000).values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input1,input2]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newguarantee(input):
    X = pd.read_csv('../clusteringResult/guarantee.csv',  usecols=['priclasecam','priclasecamlabel'])  # 读取训练数据
    data_train=X[['priclasecam']].values
    label_train=X[['priclasecamlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newinvestment(input):
    X = pd.read_csv('../clusteringResult/investment.csv',  usecols=['investnum','investnumlabel'])  # 读取训练数据
    data_train=X[['investnum']].values
    label_train=X[['investnumlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newbid(input):
    X = pd.read_csv('../clusteringResult/bid.csv',  usecols=['bidnum','bidnumlabel'])  # 读取训练数据
    data_train=X[['bidnum']].values
    label_train=X[['bidnumlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newrecruit(input):
    X = pd.read_csv('../clusteringResult/recruit.csv',  usecols=['recruitnum','recruitnumlabel'])  # 读取训练数据
    data_train=X[['recruitnum']].values
    label_train=X[['recruitnumlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newinsurance(input):
    X = pd.read_csv('../clusteringResult/insurance.csv',  usecols=['cbrq','cbrqlabel'])  # 读取训练数据
    data_train=X[['cbrq']].values
    label_train=X[['cbrqlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newsecurity(input1,input2,input3,input4,input5):
    X = pd.read_csv('../clusteringResult/security.csv',  usecols=['unpaidsocialins_so110','unpaidsocialins_so210','unpaidsocialins_so310','unpaidsocialins_so410','unpaidsocialins_so510','securitylabel'])  # 读取训练数据
    data_train=X[['unpaidsocialins_so110','unpaidsocialins_so210','unpaidsocialins_so310','unpaidsocialins_so410','unpaidsocialins_so510']].head(10000).values
    label_train=X[['securitylabel']].head(10000).values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input1,input2,input3,input4,input5]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newquality(input):
    X = pd.read_csv('../clusteringResult/quality.csv',  usecols=['passpercent','passpercentlabel'])  # 读取训练数据
    data_train=X[['passpercent']].values
    label_train=X[['passpercentlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newamount(input):
    X = pd.read_csv('../clusteringResult/amount.csv',  usecols=['enforce_amount','amountlabel'])  # 读取训练数据
    data_train=X[['enforce_amount']].values
    label_train=X[['amountlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newabnormal(input):
    X = pd.read_csv('../clusteringResult/abnormal.csv',  usecols=['is_except','abnormalnumlabel'])  # 读取训练数据
    data_train=X[['is_except']].values
    label_train=X[['abnormalnumlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newpunish(input):
    X = pd.read_csv('../clusteringResult/punish.csv',  usecols=['punish','punishlabel'])  # 读取训练数据
    data_train=X[['punish']].values
    label_train=X[['punishlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newrightpledge(input):
    X = pd.read_csv('../clusteringResult/rightpledge.csv',  usecols=['pledgenum','pledgenumlabel'])  # 读取训练数据
    data_train=X[['pledgenum']].values
    label_train=X[['pledgenumlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newtaxunpaid(input):
    X = pd.read_csv('../clusteringResult/taxunpaid.csv',  usecols=['taxunpaidnum','taxunpaidnumlabel'])  # 读取训练数据
    data_train=X[['taxunpaidnum']].values
    label_train=X[['taxunpaidnumlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newcreditgrade(input):
    X = pd.read_csv('../clusteringResult/creditgrade.csv',  usecols=['credit_grade','credit_gradelabel'])  # 读取训练数据
    data_train=X[['credit_grade']].values
    label_train=X[['credit_gradelabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newcredit(input):
    X = pd.read_csv('../clusteringResult/credit.csv',  usecols=['is_justice_credit','is_justice_creditlabel'])  # 读取训练数据
    data_train=X[['is_justice_credit']].values
    label_train=X[['is_justice_creditlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newbrandnum(input):
    X = pd.read_csv('../clusteringResult/brandnum.csv',  usecols=['ibrand_num','ibrand_numlabel'])  # 读取训练数据
    data_train=X[['ibrand_num']].values
    label_train=X[['ibrand_numlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newcopynum(input):
    X = pd.read_csv('../clusteringResult/copynum.csv',  usecols=['icopy_num','icopy_numlabel'])  # 读取训练数据
    data_train=X[['icopy_num']].values
    label_train=X[['icopy_numlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newpatentnum(input):
    X = pd.read_csv('../clusteringResult/patentnum.csv',  usecols=['ipat_num','ipat_numlabel'])  # 读取训练数据
    data_train=X[['ipat_num']].values
    label_train=X[['ipat_numlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

def newdomnum(input):
    X = pd.read_csv('../clusteringResult/domnum.csv',  usecols=['idom_num','idom_numlabel'])  # 读取训练数据
    data_train=X[['idom_num']].values
    label_train=X[['idom_numlabel']].values
    knn=KNeighborsClassifier()
    knn.fit(data_train,label_train)
    X_test=[input]
    X_test = np.array(X_test).reshape(1, -1)
    result=knn.predict(X_test)
    return result

