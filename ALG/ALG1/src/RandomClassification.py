import numpy as np
from sklearn import svm,neighbors,tree
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer as TF
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


logging.basicConfig(level=logging.INFO)
Logger = logging.getLogger('RandomClf.stdout')
Logger.setLevel("INFO")


def Classification(MalwareCorpus, GoodwareCorpus, TestSize, FeatureOption, Model, NumTopFeats):
    '''
    Train a classifier for classifying malwares and goodwares using Support Vector Machine technique.
    Compute the prediction accuracy and f1 score of the classifier.
    Modified from Jiachun's code.

    :param String MalwareCorpus: absolute path of the malware corpus
    :param String GoodwareCorpus: absolute path of the goodware corpus
    :param String FeatureOption: tfidf or binary, specify how to construct the feature vector

    :rtype String Report: result report
    '''
    # step 1: creating feature vector
    Logger.debug("Loading Malware and Goodware Sample Data")
    AllMalSamples = CM.ListFiles(MalwareCorpus, ".data")
    # print(len(AllMalSamples))
    AllGoodSamples = CM.ListFiles(GoodwareCorpus, ".data")
    AllSampleNames = AllMalSamples + AllGoodSamples
    Logger.info("Loaded samples")

    FeatureVectorizer = TF(input='filename', tokenizer=lambda x: x.split('\n'), token_pattern=None,
                           binary=FeatureOption)
    x = FeatureVectorizer.fit_transform(AllMalSamples + AllGoodSamples)
    print(x.shape)

    # label malware as 1 and goodware as -1
    # Mal_labels = np.ones(len(AllMalSamples))
    # Good_labels = np.empty(len(AllGoodSamples))
    # Good_labels.fill(-1)
    # y = np.concatenate((Mal_labels, Good_labels), axis=0)
    # Logger.info("Label array - generated")

    acc = []
    pre = []
    reca = []
    f1 = []
    auc = []
    for i in range(1):
    # step 2: split all samples to training set and test set
        x_train_samplenames, x_test_samplenames, y_train, y_test = train_test_split(AllSampleNames, y, test_size=TestSize,random_state=0)
        print("x_train_samplenames--- ")
        x_train = FeatureVectorizer.fit_transform(x_train_samplenames)
        print(type(x_train))
        print(x_train)

        # x_test = FeatureVectorizer.transform(x_test_samplenames)
        # Logger.debug("Test set split = %s", TestSize)
        # Logger.info("train-test split done")


        # Clf = RandomForestClassifier().fit(x_train,y_train)
        # Clf = LinearSVC().fit(x_train, y_train)
        # Clf = BernoulliNB().fit(x_train, y_train)
        # Clf = LogisticRegression().fit(x_train, y_train)
        # Clf = neighbors.KNeighborsClassifier().fit(x_train, y_train)
        # Clf = tree.DecisionTreeClassifier().fit(x_train, y_train)

        # y_predict = Clf.predict(x_test)
        # acc.append(np.mean(y_predict == y_test))
        # pre.append(metrics.precision_score(y_test, y_predict))
        # reca.append(metrics.recall_score(y_test, y_predict))
        # f1.append(metrics.f1_score(y_test, y_predict))
        # auc.append(metrics.roc_auc_score(y_test, y_predict))
        # print("------- \n", metrics.confusion_matrix(y_test, y_predict))


    # print("acc--- ", np.mean(np.array(acc)))
    # print("pre--- ", np.mean(np.array(pre)))
    # print("reca--- ", np.mean(np.array(reca)))
    # print("f1--- ", np.mean(np.array(f1)))
    # print("auc--- ", np.mean(np.array(auc)))




if __name__=='__main__':
    NCpuCores = 3
    TestSize = 0.3
    FeatureOption = True
    NumFeatForExp = 10
    MalDir = r'D:\Python\python-src\drebin-master\malware'
    GoodDir = r'D:\Python\python-src\drebin-master\benign'
    # GetApkData(NCpuCores, MalDir,GoodDir)
    Classification(MalDir, GoodDir, TestSize, FeatureOption, LinearSVC, NumFeatForExp)