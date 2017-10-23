import pandas
from sklearn.model_selection import train_test_split


def run():
    data_file_name = "data/random.xlsx"
    df = pandas.read_excel(data_file_name)
    X = df
    y = df.loc[:, 'rank':]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=35)
    X_test = X_test.loc[:, :"label4"]
    X_list = []
    y_list = []
    clf_list = []
    x1 = X_train.loc[X_train['rank'] != 1]
    x1['rating'] = 30
    print(x1)
    for i in range(1,20):
        xi = X_train.loc[X_train['rank'] == i]
        xj = X_train.loc[X_train['rank'] != i]
        X_train = xj
        xi['ingroup'] = 1
        xj['ingroup'] = 0
        xij = xi.aapend(xj)
        X_list.append(xij.loc[:,:'label4'])
        y_list.append(xij.loc[:,'ingroup':])

        pass


    pass


def preparation(X_train, y_train):
    pass


if __name__ == '__main__':
    run()