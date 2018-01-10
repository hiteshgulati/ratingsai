import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.svm import SVC
from sklearn.metrics import f1_score


def run():
    data_file_name = "data/dataset2.xlsx"
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
    labels = list(data)
    labels = labels[3:]

    X1 = data1[labels]
    y1 = data1.RatingID
    y1 = y1.replace(3,2)
    y1 = y1.replace(4,2)
    y1 = y1.replace(5,2)
    y1 = y1.replace(6,2)
    clf1.fit(X1,y1)

    X2 = data2[labels]
    y2 = data2.RatingID
    y2 = y2.replace(4, 3)
    y2 = y2.replace(5, 3)
    y2 = y2.replace(6, 3)
    clf2.fit(X2, y2)

    X3 = data3[labels]
    y3 = data3.RatingID
    y3 = y3.replace(5, 4)
    y3 = y3.replace(6, 4)
    clf3.fit(X3, y3)

    X4 = data4[labels]
    y4 = data4.RatingID
    y4 = y4.replace(6, 5)
    clf4.fit(X4, y4)

    X5 = data5[labels]
    y5 = data5.RatingID
    clf5.fit(X5, y5)

    X_test = data_test[labels]
    y_test = data_test.RatingID
    y_pred = y_test.copy()
    for i, item in X_test.iterrows():
            if clf1.predict([item]) == 1:
                y_pred[i] = 1
            elif clf2.predict([item]) == 2:
                y_pred[i] = 2
            elif clf3.predict([item]) == 3:
                y_pred[i] = 3
            elif clf4.predict([item]) == 4:
                y_pred[i] = 4
            elif clf5.predict([item]) == 5:
                y_pred[i] = 5
            else:
                y_pred[i] = 6

    score = f1_score(y_test, y_pred, average='micro')
    print(score)



    pass


def preparation(X_train, y_train):
    pass


if __name__ == '__main__':
    run()