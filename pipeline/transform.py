def clean_data(sales):
    for sale in sales:
        sale['order_id'] = sale['order_id'].strip()
        sale['customer_id'] = sale['customer_id'].strip()
        sale['product_name'] = sale['product_name'].strip()
        sale['quantity'] = sale['quantity'].strip()
        sale['unit_price'] = sale['unit_price'].strip()
        sale['sale_date'] = sale['sale_date'].strip()
        sale['payment_method'] = sale['payment_method'].strip()
        sale['city'] = sale['city'].strip()
    return sales