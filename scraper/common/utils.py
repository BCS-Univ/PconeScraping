import re

class Utils:
    '''Utils class for processing data
    '''

    def process_shop_info(self, shop_info: list) -> tuple:
        '''Extract the text of every line of the raw html

        Args:
            shop_info (list): list of shop info

        Returns:
            tuple: tuple of shop info
        '''
        try:
            return tuple(info.text for info in shop_info)
        except Exception as e:
            print(f"Error occurred while processing shop info: {e}")
            return ()

    def process_product_money(self, product_money: str) -> int:
        '''Extract the numerical value from the product money string

        Args:
            product_money (str): product money string

        Returns:
            int: processed product money
        '''
        try:
            return int(product_money.split('$')[1])
        except Exception as e:
            print(f"Error occurred while processing product money {product_money}: {e}")
            return None

    def process_product_score(self, product_score: str) -> str:
        '''Extract the score from the product score string

        Args:
            product_score (str): product score string

        Returns:
            str: processed product score
        '''
        try:
            return product_score.split('(')[0]
        except Exception as e:
            print(f"Error occurred while processing product score {product_score}: {e}")
            return None

    def calculate_discount(self, product_money: int, yuan: int) -> int:
        '''Calculate the discount percentage

        Args:
            product_money (int): product money value
            yuan (int): yuan value

        Returns:
            int: discount percentage
        '''
        try:
            return int(product_money / yuan * 100)
        except Exception as e:
            print(f"Error occurred while calculating discount: {e}")
            return None

    def get_buy_count(self, buy_info: str) -> str:
        '''Get the amount of people who bought the product

        Args:
            buy_info (str): buy info string

        Returns:
            str: the number of people
        '''
        try:
            buy = re.findall(r"\d+.?\d*", buy_info)
            return buy[2] if len(buy) > 2 else '0'
        except Exception as e:
            print(f"Error occurred while processing buy count {buy_info}: {e}")
            return '0'

    def runAll(self, product_info: dict) -> None:
        '''Process all the product information and return the result as a list

        Args:
            product_info (dict): dictionary containing the product information

        Returns:
            None
        '''
        shop_name = product_info['shop_name']
        product_name = product_info['product_name']

        shop_q, shop_s, shop_t, shop_r = self.process_shop_info(product_info['shop_info'])
        product_money = self.process_product_money(product_info['product_money'])
        product_score = self.process_product_score(product_info['product_score'])
        yuan = product_money

        zhe = self.calculate_discount(product_money, yuan)
        buy_count = self.get_buy_count(product_info['buy_info'])
        return [shop_name, product_name, shop_q, shop_s, shop_t, shop_r, product_money, zhe, product_score, buy_count]
