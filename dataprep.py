import pandas as pd
import os


def run():
    crisil_file_path = os.path.join(os.getcwd(),'crisil')
    list_of_alphabet_files = os.listdir(crisil_file_path)
    a_file = list_of_alphabet_files[0]
    df_complete = pd.read_csv(os.path.join(crisil_file_path, a_file))
    df_complete = df_complete.dropna()

    for each_alphabet_file in list_of_alphabet_files[1:18]:
        print(each_alphabet_file, "_________________")
        df = pd.read_csv(os.path.join(crisil_file_path,each_alphabet_file))
        df = df.dropna()
        print(df.describe())
        df_complete = df_complete.append(df)
    print(df_complete.describe())



    pass



if __name__ == '__main__':
    run()