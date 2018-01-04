# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen as u_req
import pandas as pd
import numpy as np
import sys

naslice = {"Company": "", "Feature": "", "Period" : "", "Error": ()}
errordf = pd.DataFrame(columns = list(naslice))
def run():
    string = "Sita Ram & Company"
    # page_url = print (url_maker(string))
    # get_containers(page_url)
    make_table()
    errordf.to_excel("data/errordf.xlsx", index = False)
    print ("Error table also made")

    pass

def make_table():
    funda = pd.read_excel("data/funda.xlsx")
    companies_list = pd.read_excel("data/final_list.xlsx")
    compl = companies_list.Quandl_Code
    slice = {"Company": "", "EBIDTMRG3": 0, "EBIDTMRG": 0, "REV3G": 0, "REV3SD": 0, "REV": 0, "TDGCA": 0, "GEARING": 0,
             "GEARINGWT": 0, "CASH": 0, "TDCASH": 0, "CFTA": 0, "EQINF3": 0, "EQ3TNW": 0, "GCA": 0, "OPCYC": 0,
             "ROCE": 0, "COB": 0, "EQ": 0, "TD": 0, "NP": 0, "RSTA": 0, "BWDR": 0, "CFO": 0, "CDS": 0, "TNW" :0}
    fundadf = pd.DataFrame(columns=list(slice))
    for item in compl:
        print(item)
        slice['Company'] = item
        slice['EBIDTMRG3'] = (value(funda,item, "EBIDTPCT", "t")  + value(funda,item, "EBIDTPCT", "t-1")
                              + value(funda,item, "EBIDTPCT", "t-2"))/3
        slice['EBIDTMRG'] = value(funda,item, "EBIDTPCT", "t")
        slice['REV3G'] = value(funda,item, "REV3", "t")
        slice['REV3SD'] = np.std([value(funda,item, "REV1", "t"), value(funda,item, "REV1", "t-1"),
                                  value(funda,item, "REV1", "t-2")])
        slice['REV'] = value(funda,item, "SR", "t")
        slice['TDGCA'] = value(funda,item, "DEBT", "t") / value(funda,item, "NCF", "t")
        slice['GEARING'] = gearing(funda, item, "t")
        slice['GEARINGWT'] = gearing(funda, item, "t")* 0.6 + gearing(funda,item,"t-1") * .3 + \
                             gearing(funda,item,"t-2") * .1
        slice['CASH'] = value(funda,item, "CASH", "t")
        slice['TDCASH'] = value(funda,item, "DEBT", "t") / value(funda,item, "CASH", "t")
        slice ['CFTA'] = value(funda,item, "NCF", "t") / value(funda,item, "TA", "t")
        slice['EQINF3'] = (value(funda,item, "EQCAP", "t") - value(funda,item, "EQCAP", "t-3")) /3
        slice['EQ3TNW'] = slice['EQINF3'] / (value(funda,item, "RSRV", "t") + value(funda,item, "EQCAP", "t"))
        slice['GCA'] = value(funda,item, "NCF", "t")
        slice['OPCYC'] = value(funda,item, "DAYWC", "t")
        slice['ROCE'] = value(funda,item, "ROCE", "t")
        slice['COB'] = value(funda,item, "FKD", "t")
        slice['EQ'] = value(funda,item, "EQCAP", "t")
        slice['TD'] = value(funda,item, "DEBT", "t")
        slice['NP'] = value(funda,item, "NP", "t")
        slice['RSTA'] = value(funda,item, "RSRV", "t") / value(funda,item, "TA", "t")
        slice['BWDR'] = value(funda,item, "DEBT", "t") / value(funda,item, "TA", "t")
        slice['CFO'] = value(funda,item, "CFO", "t")
        slice['CDS'] = value(funda,item, "CREDIT", "t")
        slice['TNW'] = value(funda,item, "RSRV", "t") + value(funda,item, "EQCAP", "t")
        fundadf = fundadf.append(slice, ignore_index= True)
        print(item, "Done!")
    fundadf.to_excel("data/fundadf.xlsx", index = False)
    print ("Done Making Table")



def value (funda, company = "20MICRONS", feature = "SR", period = "t"):
    try:
        retvalue = funda[(funda.Company == company) & (funda.Feature == feature) & (funda.Period == period)].Adj_Value.iloc[0]
    except:
        naslice['Company'] = company
        naslice['Feature'] = feature
        naslice['Period'] = period
        naslice['Error'] = sys.exc_info()
        global errordf
        errordf = errordf.append(naslice, ignore_index = "True")
        retvalue = 1
    return retvalue

def gearing (funda, company = "20MICRONS", period = "t"):
    return value(funda,company, "DEBT", period) / \
           (value(funda, company, "RSRV", period) + value(funda,company, "EQCAP", period))


# def get_listed_companies(containers):
#     c = {}
#     flag = 0
#     cin = ""
#     for item_tag in containers:
#         item = str(item_tag)
#         if flag == 1:
#             c[cin] = item[4:-5]
#             flag = 0
#         if item[:5] == "<h5>L" and len(item) == 30 :
#             cin = item[4:-5]
#             flag = 1
#     return c
#
# def create_list ():
#     company_list = pd.read_excel("data/final_list.xlsx")
#     for i, index in company_list.iterrows():




# def get_containers(page_url):
#     u_client = u_req(page_url, timeout=10)
#     page_html = u_client.read()
#     u_client.close()
#     page_soup = soup(page_html, 'html.parser')
#     containers = page_soup.findAll("h5")
#     return containers
#
# def url_maker(search_string):
#     base_url = "https://www.zaubacorp.com/companysearchresults/"
#     search_string_url = ""
#     for e in search_string:
#         if e.isalnum():
#             search_string_url += e.lower()
#         else:
#             search_string_url += "-"
#     search_url = base_url + search_string_url
#     return search_url
#
#     pass



if __name__ == '__main__':
    run()