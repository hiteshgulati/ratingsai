# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen as u_req
import pandas as pd


def run():
    string = "Sita Ram & Company"
    # page_url = print (url_maker(string))
    # get_containers(page_url)

    pass

def make_table():
    funda = pd.read_excel("data/funda.xlsx")
    companies_list = pd.read_excel("data/final_list.xlsx")
    compl = companies_list.Quandl_Code
    slice = {"Company": "", "EBIDTMRG3": 0, "EBIDTMRG": 0, "REV3G": 0, "REV3SD": 0, "REV": 0, "TDGCA": 0, "GEARING": 0,
             "GEARINGWT": 0, "CASH": 0, "TDCASH": 0, "CFTA": 0, "EQINF3": 0, "EQ3TNW": 0, "GCA": 0, "OPCYC": 0,
             "ROCE": 0, "COB": 0, "EQ": 0, "TD": 0, "NP": 0, "RSTA": 0, "BWDR": 0, "CFO": 0, "CDS": 0}
    for item in compl:
        slice['Company'] = item
        slice['EBIDTMRG3'] = (funda[(funda.Company == item) & (funda.Feature == "EBIDTPCT") &
                                    (funda.Period == "t")].Adj_Value.iloc[0] +
                              funda[(funda.Company == item) & (funda.Feature == "EBIDTPCT") & (
                              funda.Period == "t-1")].Adj_Value.iloc[0] +
                              funda[(funda.Company == item) & (funda.Feature == "EBIDTPCT") &
                                    (funda.Period == "t-2")].Adj_Value.iloc[0])/3
        slice['EBIDTMRG'] = funda[(funda.Company == item) & (funda.Feature == "EBIDTPCT") & (funda.Period == "t")].Adj_Value.iloc[0]
        slice['REV3G'] = funda[(funda.Company == item) & (funda.Feature == "REV3") &
                               (funda.Period == "t")].Adj_Value.iloc[0]

        pass




def get_listed_companies(containers):
    c = {}
    flag = 0
    cin = ""
    for item_tag in containers:
        item = str(item_tag)
        if flag == 1:
            c[cin] = item[4:-5]
            flag = 0
        if item[:5] == "<h5>L" and len(item) == 30 :
            cin = item[4:-5]
            flag = 1
    return c

def create_list ():
    company_list = pd.read_excel("data/final_list.xlsx")
    for i, index in company_list.iterrows():




def get_containers(page_url):
    u_client = u_req(page_url, timeout=10)
    page_html = u_client.read()
    u_client.close()
    page_soup = soup(page_html, 'html.parser')
    containers = page_soup.findAll("h5")
    return containers

def url_maker(search_string):
    base_url = "https://www.zaubacorp.com/companysearchresults/"
    search_string_url = ""
    for e in search_string:
        if e.isalnum():
            search_string_url += e.lower()
        else:
            search_string_url += "-"
    search_url = base_url + search_string_url
    return search_url

    pass



if __name__ == '__main__':
    run()