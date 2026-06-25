import csv

RAW_SALES_FILE = "data/raw/sales_sample.csv"

def read_sales ():

    with open(RAW_SALES_FILE, "r", encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        sales = list(reader)

        return sales



