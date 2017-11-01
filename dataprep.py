import pandas as pd
import os
from difflib import SequenceMatcher


def run():
    # crisil_file_path = os.path.join(os.getcwd(),'crisil')
    # list_of_alphabet_files = os.listdir(crisil_file_path)
    # a_file = list_of_alphabet_files[0]
    # df_complete = pd.read_csv(os.path.join(crisil_file_path, a_file))
    # df_complete = df_complete.dropna()
    #
    # for each_alphabet_file in list_of_alphabet_files[1:]:
    #     df = pd.read_csv(os.path.join(crisil_file_path,each_alphabet_file))
    #     total_records = df.shape
    #     df = df.dropna()
    #     trimmed_records = df.shape
    #     df_complete = df_complete.append(df)
    #     print(each_alphabet_file, ":: ", total_records, "--> ", trimmed_records, "++--> ", df_complete.shape)
    # print(df_complete.describe())
    # df_complete.to_csv(path_or_buf=os.path.join(crisil_file_path,"aacompletefile.csv"), index=False)



    pass


def company_matching(threshold= .8):
    file_path = os.getcwd()
    file_name = "crisil ratings.xlsx"
    crisil_df = pd.read_excel(os.path.join(file_path,file_name), sheetname="allcrisil")
    nse_df = pd.read_excel(os.path.join(file_path,file_name), sheetname="allnse")
    combined_df = pd.DataFrame(columns=list(crisil_df))
    combined_df['company_nse'] = None
    combined_df['code_nse'] = None
    unused_crisil = pd.DataFrame(columns=list(crisil_df))
    unused_nse = pd.DataFrame(columns=list(nse_df))
    for index_nse, item_nse in nse_df.iterrows():
        for index_crisil, item_crisil in crisil_df.iterrows():
            if SequenceMatcher(None,item_nse['company_nse'], item_crisil['company']).ratio() >= threshold:
                item_crisil['company_nse'] = item_nse['company_nse']
                item_crisil['code_nse'] = item_nse['code_nse']






if __name__ == '__main__':
    run()