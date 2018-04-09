from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as url_req
import pandas as pd

crisil_search_page = "https://www.crisil.com/en/home/Search-Result-Page."


def run():
    #make_crisil_code_file(source_file = "data/listed_companies.xlsx")

    # print(get_company_code("alacrity securities limited"))
    pass


def make_crisil_code_file (source_file = "data/listed_companies.xlsx"):
    list = pd.read_excel(source_file)
    for index, slice in list.iterrows():
        try:
            company_crisil_code = get_company_code(slice.company_name)
        except:
            company_crisil_code = None
        list['company_crisil_code'][index] = company_crisil_code
        print(index)
    list.to_excel(source_file)
    print(list)
    pass


def make_search_url(company_name = "vip industries limited"):
    compatible_string = company_name.replace(' ', '%20')
    search_url = crisil_search_page + compatible_string + ".html"
    return (search_url)
    pass


def get_company_code (company_name = "vip industries limited"):
    search_url  = make_search_url(company_name)
    url_client = url_req(search_url)
    page_html = url_client.read()
    url_client.close()
    page_soup = soup(page_html,'html.parser')
    tag = page_soup.find_all(lambda tag: tag.name.lower()=='p',
                             string=lambda x: x and x.lower()==company_name.lower())[0]
    link = tag.parent['href']
    company_code = link[link.find('.')+1: link.find('.', link.find('.')+1)]
    return company_code


if __name__ == '__main__':
    run()