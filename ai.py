from datetime import datetime
start_time = datetime.now()

from sklearn.decomposition import  PCA
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.svm import SVC
from sklearn.metrics import f1_score


def run( pca_components = 5):
    data_file_name = "data/dataset.xlsx"
    data = pd.read_excel(data_file_name)
    data1, data_test = tts(data, test_size=0.2)
    data2 = data1[data1.RatingID != 1]
    data3 = data2[data2.RatingID != 2]
    data4 = data3[data3.RatingID != 3]
    data5 = data4[data4.RatingID != 4]
    clf1 = SVC()
    clf2 = SVC()
    clf3 = SVC()
    clf4 = SVC()
    clf5 = SVC()
    pca1 = PCA(n_components=pca_components)
    pca2 = PCA(n_components=pca_components)
    pca3 = PCA(n_components=pca_components)
    pca4 = PCA(n_components=pca_components)
    pca5 = PCA(n_components=pca_components)
    labels = list(data)
    labels = labels[3:]

    X1 = data1[labels]
    X1 = pca1.fit_transform(X1)
    y1 = data1.RatingID
    y1 = y1.replace(3,2)
    y1 = y1.replace(4,2)
    y1 = y1.replace(5,2)
    y1 = y1.replace(6,2)
    clf1.fit(X1,y1)

    X2 = data2[labels]
    X2 = pca2.fit_transform(X2)
    y2 = data2.RatingID
    y2 = y2.replace(4, 3)
    y2 = y2.replace(5, 3)
    y2 = y2.replace(6, 3)
    clf2.fit(X2, y2)

    X3 = data3[labels]
    X3 = pca3.fit_transform(X3)
    y3 = data3.RatingID
    y3 = y3.replace(5, 4)
    y3 = y3.replace(6, 4)
    clf3.fit(X3, y3)

    X4 = data4[labels]
    X4 = pca4.fit_transform(X4)
    y4 = data4.RatingID
    y4 = y4.replace(6, 5)
    clf4.fit(X4, y4)

    X5 = data5[labels]
    X5 = pca5.fit_transform(X5)
    y5 = data5.RatingID
    clf5.fit(X5, y5)

    X_test = data_test[labels]
    y_test = data_test.RatingID
    y_pred = y_test.copy()
    for i, item in X_test.iterrows():
            if clf1.predict(pca1.transform([item])) == 1:
                y_pred[i] = 1
            elif clf2.predict(pca2.transform([item])) == 2:
                y_pred[i] = 2
            elif clf3.predict(pca3.transform([item])) == 3:
                y_pred[i] = 3
            elif clf4.predict(pca4.transform([item])) == 4:
                y_pred[i] = 4
            elif clf5.predict(pca5.transform([item])) == 5:
                y_pred[i] = 5
            else:
                y_pred[i] = 6

    score = f1_score(y_test, y_pred, average='micro')
    # print(score)
    # print(datetime.now() - start_time)
    return (score)


    pass


def preparation(X_train, y_train):
    pass


if __name__ == '__main__':
    n_iterations = 20
    l = [0] * 26
    for n in range (n_iterations):
        for i in range (1,27):
            print(n, i)
            l[i-1] += run(i)
    for i in range(26):
        print (i, "--> ", l[i]/20)