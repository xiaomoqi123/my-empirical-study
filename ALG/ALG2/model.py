import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold,cross_val_score,train_test_split
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn import svm,neighbors,tree
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split,cross_val_score,cross_validate
from sklearn import metrics
from sklearn.feature_selection import SelectKBest,chi2,f_classif
from minepy import MINE
from numpy import array


def mic(x, y):
    m = MINE()
    m.compute_score(x, y)
    return (m.mic(), 0.5)

# label malware as 1 and goodware as -1
X=np.loadtxt("./result/2_gram.csv",skiprows=1, delimiter=',', dtype=int)
# print(X)
origin = pd.read_csv("./result/data.csv")
# y = origin["isMalware"]
# print(np.array(list(y)))

acc = []
pre = []
reca = []
f1 = []
auc = []
for i in range(1):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    # clf = svm.SVC()
    clf = svm.LinearSVC()
    # clf = LogisticRegression()
    # clf = GradientBoostingClassifier()
    # clf = neighbors.KNeighborsClassifier(n_neighbors=5)
    # clf = RandomForestClassifier()
    # clf = BernoulliNB()
    # clf = tree.DecisionTreeClassifier()
    X_new = SelectKBest(lambda X, Y: array( list(map(lambda x: mic(x, Y), X.T)) ).T, k=2).fit_transform(X_train, y_train)
    # X_new = SelectKBest(chi2, k=5).fit_transform(X_train, y_train)
    print(X_new[0,:])

    # clf.fit(X_train, y_train)
    # y_predict = clf.predict(X_test)
    # print(metrics.precision_score(y_test,y_predict))
    # acc.append(np.mean(y_predict==y_test))
    # pre.append(metrics.precision_score(y_test,y_predict))
    # reca.append(metrics.recall_score(y_test,y_predict))
    # f1.append(metrics.f1_score(y_test,y_predict))
    # auc.append(metrics.roc_auc_score(y_test,y_predict))
    # print("------- \n",metrics.confusion_matrix(y_test,y_predict))

# print("acc--- ",np.mean(np.array(acc)))
# print("pre--- ",np.mean(np.array(pre)))
# print("reca--- ",np.mean(np.array(reca)))
# print("f1--- ",np.mean(np.array(f1)))
# print("auc--- ",np.mean(np.array(auc)))
