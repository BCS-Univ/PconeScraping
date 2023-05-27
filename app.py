from scraper.pconeScraper import PconeScraper
from scraper.common.export import export_csv


def main():
    scraper = PconeScraper("https://www.pcone.com.tw/product/603#ref=d_nav")
    scraper.run()
    export_csv(scraper.data, "pcone.csv")

if __name__ == '__main__':
    main()