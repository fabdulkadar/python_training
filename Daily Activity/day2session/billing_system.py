''' Function for a billing system that calculates the total bill amunt from price and quantity, also discount if any'''

def bill_gen(prod_price, prod_quantity, prod_discount=0):
    total_price = prod_price * prod_quantity
    discount_price = total_price - (total_price*(prod_discount/100))
    print (f"Product Price = {prod_price} | Product Quantity = {prod_quantity} | Discount Percentage = {prod_discount} | Final Price = {discount_price}")

if __name__=="__main__":
    bill=bill_gen(50,5,25)
