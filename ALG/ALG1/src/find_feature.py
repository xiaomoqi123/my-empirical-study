import numpy as np
from sklearn import svm,neighbors,tree
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer as TF
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
import logging
import random
import src.CommonModules as CM
import operator




def Classification(MalwareCorpus, GoodwareCorpus, TestSize, FeatureOption, Model, NumTopFeats):
    AllMalSamples = CM.ListFiles(MalwareCorpus, ".data")
    # print(len(AllMalSamples))
    # AllGoodSamples = CM.ListFiles(GoodwareCorpus, ".data")
    # AllSampleNames = AllMalSamples + AllGoodSamples


    # FeatureVectorizer = TF(input='filename', tokenizer=lambda x: x.split('\n'), token_pattern=None,
    #                        max_features=None, vocabulary=None, binary=False, use_idf=False )

    # x = FeatureVectorizer.fit_transform(AllMalSamples)
    Count_word = CountVectorizer(input='filename', tokenizer=lambda x: x.split('\n'), token_pattern=None)
    x = Count_word.fit(AllMalSamples)
    # print(x.shape)
    # print(x.vocabulary_)

    # a =[2,4,9,1,5]
    # t = sorted(a, reverse=True)
    # print(t)
    res = sorted(x.vocabulary_.items(), key=operator.itemgetter(0),reverse=True)#按照值进行降序排列
    print(res[0:21])


    # for i in range(1):
    #     # step 2: split all samples to training set and test set
    #     # x_train_samplenames, x_test_samplenames, y_train, y_test = train_test_split(AllMalSamples, y, test_size=TestSize,random_state=0)
    #     print("x_train_samplenames--- ")
    #     x_train = FeatureVectorizer.fit_transform(x_train_samplenames)
    #     print(type(x_train))
    #     print(x_train)
    #



if __name__=='__main__':
    NCpuCores = 3
    TestSize = 0.3
    FeatureOption = True
    NumFeatForExp = 10
    MalDir = r'F:\gxt\副本\signature\signature-virustotal-malware'
    GoodDir = r'D:\Python\python-src\drebin-master\benign'
    # GetApkData(NCpuCores, MalDir,GoodDir)
    Classification(MalDir, GoodDir, TestSize, FeatureOption, LinearSVC, NumFeatForExp)