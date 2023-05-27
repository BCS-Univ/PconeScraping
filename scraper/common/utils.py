import re

class Utils:
    def process_shop_info(self, shop_info: list) -> tuple:
        try:
            return tuple(info.text for info in shop_info)
        except Exception as e:
            print(f"在處理店家資訊時發生錯誤: {e}")
            return ()

    def process_product_money(self, product_money: str) -> int:
        try:
            return int(product_money.split('$')[1])
        except Exception as e:
            print(f"在處理商品價格{product_money}時發生錯誤: {e}")
            return None

    def process_product_score(self, product_score: str) -> str:
        try:
            return product_score.split('(')[0]
        except Exception as e:
            print(f"在處理商品評分{product_score}時發生錯誤: {e}")
            return None

    def calculate_discount(self, product_money: int, yuan: int) -> int:
        try:
            return int(product_money / yuan * 100)
        except Exception as e:
            print(f"在計算商品折數時發生錯誤: {e}")
            return None

    def get_buy_count(self, buy_info: str) -> str:
        try:
            buy = re.findall(r"\d+.?\d*", buy_info)
            return buy[2] if len(buy) > 2 else '0'
        except Exception as e:
            print(f"在處理購買人數{buy_info}時發生錯誤: {e}")
            return '0'

    def runAll(self, product_info: dict) -> None:
        shop_name = product_info['shop_name']
        product_name = product_info['product_name']

        shop_q, shop_s, shop_t, shop_r = self.process_shop_info(product_info['shop_info'])
        product_money = self.process_product_money(product_info['product_money'])
        product_score = self.process_product_score(product_info['product_score'])
        yuan = product_money

        zhe = self.calculate_discount(product_money, yuan)
        buy_count = self.get_buy_count(product_info['buy_info'])
        return [shop_name, product_name, shop_q, shop_s, shop_t, shop_r, product_money, zhe, product_score, buy_count]
