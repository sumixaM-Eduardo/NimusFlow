import csv

RAW_SALES_FILE = "data/raw/sales_sample.csv"

def extract():
    with open(RAW_SALES_FILE, "r", encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        sales = list(reader)
        return sales