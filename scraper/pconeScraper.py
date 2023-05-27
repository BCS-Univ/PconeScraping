import requests
from bs4 import BeautifulSoup
from scraper.common.utils import Utils

class PconeScraper():
    '''Main scraper class for pcone.com.tw
    '''
    def __init__(self, url: str) -> None:
        self.url = url
        self.data = []
        self.header = {'content-type': 'text/plain;charset=UTF-8','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        self.src = requests.get(self.url, headers=self.header)

    def getProductsList(self) -> list:
        '''Get all products url from the page

        Returns:
            list: list of products url
        '''
        try:
            page = BeautifulSoup(self.src.text, "html.parser")
            products = page.find_all('a', class_='product-list-item')
            return ['https://www.pcone.com.tw/' + products[i].get('href') for i in range(len(products) // 8)]       #extract 25 links(200 divided by 8)
        except Exception as e:
            print('Error during getProductsList(): ', e)
            return None

    def getProductsInfo(self, product_url: str) -> dict:
        '''Get product info from the product url

        Args:
            product_url (str): one of the product url

        Returns:
            dict: raw product info
        '''
        try:
            src = requests.get(product_url, headers=self.header, verify=False)
            productPage = BeautifulSoup(src.text, 'html.parser')

            product_info = {
                'shop_name': productPage.find('div', class_='merchant-name').text,
                'product_name': productPage.find('h1', class_='name x-large-font').text,
                'shop_info': productPage.find_all("p", class_="data medium-font"),
                'product_money': productPage.find("div", class_="site-color medium-font site-color").text,
                'product_score': productPage.find("div", "review pointer").text,
                'buy_info': productPage.find("div", class_="review-info d-flex justify-content-start").text,
            }
            return product_info
        except Exception as e:
            print(f'Error during product url: {product_url} of getMerchInfo()\n', e)
            return None

    def run(self) -> None:
        '''Main function to run the scraper
        '''
        utils = Utils()
        productsUrlList = self.getProductsList()
        for product_url in productsUrlList:
            product_info = self.getProductsInfo(product_url)
            self.data.append(utils.runAll(product_info))
            print(self.data[-1])