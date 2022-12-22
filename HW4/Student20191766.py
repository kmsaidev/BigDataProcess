import numpy as np
import operator
import os
import sys

def createDataSet(folder_path):
    files = os.listdir(folder_path)
    X = []
    labels = []
    for file in files :
        labels.append(file[0])
        file_path = folder_path + '/' + file
        with open(file_path, 'r', encoding = 'UTF8') as f :
            tmp = f.readlines()
        tmp = [t[:-1] for t in tmp]
        tmp = ''.join(tmp)
        tmp = [float(t) for t in tmp]
        X.append(tmp)
    X = np.array(X)
    
    return X, labels

def classify0(inX, dataSet, labels, k):
# 거리 계산 (Euclidian distance)
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1) # 주어진 axis로 배열 요소들의 합계 반환
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort() # 배열 소팅 후 인덱스 반환
    classCount = {}
    for i in range(k): # 가장 짧은 거리를 투표
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), # 아이템 정렬
            key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def calculate_error(X_train, y_train, X_test, y_test, k) :
    error_count = 0
    for i in range(len(X_test)) :
        predict = classify0(X_test[i], X_train, y_train, k)
        if predict != y_test[i] :
            error_count += 1
    print(int(error_count/len(X_test)*100))

X_train, y_train = createDataSet(sys.argv[1])
X_test, y_test = createDataSet(sys.argv[2])

for k in range(1, 21) :
    calculate_error(X_train, y_train, X_test, y_test, k)
