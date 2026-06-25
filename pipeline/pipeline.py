import logging
import csv

RAW_SALES_FILE = "data/raw/sales_sample.csv"

def extract():
    logging.info('Extracting data from csv')
    with open(RAW_SALES_FILE, "r", encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        sales = list(reader)
    logging.info(f'extracted: {len(sales)} records')
    return sales