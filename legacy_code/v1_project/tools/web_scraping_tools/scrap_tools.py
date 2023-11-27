"""
Libs
"""
import requests
from bs4 import BeautifulSoup
import datetime

"""
-- format functions
"""
def format_string(text):
    _formated_text= (
        text
        .replace(',', '')
        .replace('.', '')
        .replace("'", "")
        .replace('—', '')
        .replace('\\', '')
        .strip()
    )
    return _formated_text

def replace_monetary(text):
    _formated_text= (
        str(text)
        .replace('£','')
        .split(')')[-1]
        .strip()
    )
    if(_formated_text == 'Tax0.00'):
        return '0.00'
    return _formated_text

def format_available_field(text):
    try:
        format_text = (
            text
            .split()[2]
            .replace('(','')
        )
        return format_text
    except:
        return text

"""
-- scrap tools
"""
def scrap_site_html(site_url):
    '''
    receive the site url as parameter
    and request the html code
    '''
    print('requesting.. -->',site_url)
    _siteResponse = requests.get(site_url)
    _soup = BeautifulSoup(_siteResponse.content,'html.parser')

    return _soup

def get_page_links(html):
    """
    when calls the function returns
    a list with all relevant links
    in the refered page.
    """
    _temp_links= []
    _html_links= (
        BeautifulSoup(str(html),'html.parser')
        .find_all('a')
    )
    for i in _html_links[::2]:
        _formated_link= (
            str(i)
            .split('"')[1]
            .replace('../','')
        )
        _temp_links.append(_formated_link)

    return _temp_links



def scrap_books_category(url):
    """
    Get all books categories from
    the index page and return as list
    """
    html_code = scrap_site_html(url)
    books_list = [] # list to store all books category

    for value in html_code.find_all('a')[4:-22]:
        #operation used to clean unwanted characters
        category_formated =(
            str(
                value
                .get('href')
                .replace('../','')
                .replace('..','')
                .replace('///','')
                .replace('//','')
            )
            .split('/')[-2]
        )

        books_list.append(category_formated)

    return books_list


def scrap_star_rating(html_code):
    '''
   return the star rating
   of the book
    '''
    formated_rating= {
        'star-rating one':'1',
        'star-rating two':'2',
        'star-rating three':'3',
        'star-rating four':'4',
        'star-rating five':'5'
    }
    _star_rating = (
        str(
            html_code
            .find_all('p')
        )
        .split('\n')[5] #step to filter the needed 'P' tag
        .split('"')[1] #steo to get the start rating
        .lower()
    )

    return formated_rating[_star_rating]

def scrap_books_attribute(base_link):
    catalog_path= 'https://books.toscrape.com/catalogue/'

    """
    get html code from the requested page
    """
    _html_code_filtered= (
        scrap_site_html(catalog_path+base_link)
    )

    """
    filter only texts from the page
    """
    _formated_str= (
        _html_code_filtered
        .get_text()
        .strip()
        .split('\n')

    )
    """
    clean blanks spaces and convert to list
    """
    _temp_list= [item.strip() for item in _formated_str if item.strip() != '']

    """
    formating the list values needed 
    """
    _final_list= {}

    _final_list['process_date']= str(datetime.datetime.now())
    _final_list['book_category']= _temp_list[4]
    _final_list['book_title']= format_string(_temp_list[6])
    _final_list['book_price']= replace_monetary(_temp_list[7])
    _final_list['book_description']= format_string(_temp_list[11])
    _final_list['upc_number']= str(_temp_list[13]).replace('UPC','')
    _final_list['product_type']= str(_temp_list[14]).replace('Product Type','').lower()
    _final_list['no_tax_price']= replace_monetary(_temp_list[15])
    _final_list['w_tax_price']= replace_monetary(_temp_list[16])
    _final_list['total_available']= format_available_field(_temp_list[19])
    _final_list['book_star']= scrap_star_rating(_html_code_filtered)

    return _final_list

def scrap_books_data(category):
    _book_data = []
    _url_base = 'http://books.toscrape.com/catalogue/category/books/'
    '''
    get html from the webpage
    and filter all elements "LI"
    '''

    books_div= (
        scrap_site_html(_url_base + category + '/index.html')
        .find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    )


    for book in books_div:
        page_links = get_page_links(book)
        for i in page_links:
            _book_data.append(scrap_books_attribute(i))


    return _book_data