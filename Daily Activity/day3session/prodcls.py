class Product:

    #constructor
    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = price * quantity
    
    #method to display product details
    def display(self):
        print(f"Product Id: {self.pid}")
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")
        print(f"Product Quantity: {self.quantity}")
        print(f"Total Price: {self.total}")

def main():
    print("Product Details")
    print("===================")
    print("Product ID\tProduct Name\tProduct Price\tProduct Quantity\tTotal Price")

    p1 = Product(101,"Laptop", 50000, 30)
    p2 = Product(102,"Mouse", 1000, 50)

    p1.display()
    p2.display()

if __name__== "__main__":
    main()

