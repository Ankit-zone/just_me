class Products:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Products.count+=1
    def get_info(self):
        print(f"product is {self.name} and price is {self.price}")
    @classmethod
    def count_products(cls):
        print(f"total no of products is = {cls.count}")
    @staticmethod
    def get_discount(price,discount):
        final_price=price-(price*discount/100)
        print(f"Final price after discount is = {final_price}")

phone=Products("phone",10000)
laptop=Products("laptop",50000)
pen=Products("pen",10)

phone.get_discount(10000,20)