import pandas as pd
import os


def run():
    crisil_file_path = os.path.join(os.getcwd(),'crisil')
    list_of_alphabet_files = os.listdir(crisil_file_path)
    a_file = list_of_alphabet_files[0]
    df_complete = pd.read_csv(os.path.join(crisil_file_path, a_file))
    df_complete = df_complete.dropna()

    for each_alphabet_file in list_of_alphabet_files[1:]:
        df = pd.read_csv(os.path.join(crisil_file_path,each_alphabet_file))
        total_records = df.shape
        df = df.dropna()
        trimmed_records = df.shape
        df_complete = df_complete.append(df)
        print(each_alphabet_file, ":: ", total_records, "--> ", trimmed_records, "++--> ", df_complete.shape)
    print(df_complete.describe())
    df_complete.to_csv(path_or_buf=os.path.join(crisil_file_path,"aacompletefile.csv"), index=False)


    pass



if __name__ == '__main__':
    run()