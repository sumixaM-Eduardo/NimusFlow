from pipeline.pipeline import extract
from pipeline.transform import clean_data, validate_data, convert_data
from pipeline.database import create_table, insert_data

def main():
    sales = extract()
    clean_sales = clean_data(sales)
    valid_data, invalid_data = convert_data(clean_sales)
    approved_data, rejected_data = validate_data(valid_data, invalid_data)
    create_table()
    insert_data(approved_data, rejected_data)

if __name__ == '__main__':
    main()
