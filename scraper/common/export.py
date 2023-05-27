import csv

def export_csv(data: list, filePath: str) -> None: 
    '''Dump the data into a csv file

    Args:
        data (list): all extracted data
        filePath (str): the path of the csv file
    '''
    try: 
        with open(filePath, 'w', newline='', encoding='utf-8-sig') as f: 
            writer = csv.writer(f) 
            writer.writerow(["店家名稱", "產品名稱", "店家商品數量", "店家評價", "店家出貨天數", "店家回覆率", "特價", "折數", "商品評分", "購買人數"]) 

            for product_data in data: 
                writer.writerow(product_data) 
    except Exception as e: 
        print(f"在寫入CSV時發生錯誤: {e}") 