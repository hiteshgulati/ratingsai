import pandas
from sklearn.model_selection import train_test_split


def run():
    data_file_name = "data/random.xlsx"
    ratings_range = 3
    df = pandas.read_excel(data_file_name,sheetname="Sheet2")
    X = df
    y = df.loc[:, 'rank':]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=35)
    X_test = X_test.loc[:, :"label4"]
    X_list = []
    y_list = []
    clf_list = []
    # x1 = X_train.loc[X_train['rank'] != 1]
    # x1['rating'] = 30
    # print(x1)
    print("____________________X_____________________")
    print(X_train)
    for i in range(1,ratings_range):
        xi = X_train.loc[X_train['rank'] == i]
        xj = X_train.loc[X_train['rank'] != i]
        X_train = xj
        xi['ingroup'] = 1
        xj['ingroup'] = 0
        xij = xi.append(xj)
        X_list.append(xij.loc[:,:'label4'])
        y_list.append(xij.loc[:,'ingroup':])
    for i in range(ratings_range-1):
        print("________________XXXXX ", i,"__________________________")
        print(X_list[i])
        print("________________yyyyy ", i, "__________________________")
        print(y_list[i])


    pass


def preparation(X_train, y_train):
    pass


if __name__ == '__main__':
    run()