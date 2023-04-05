from Product import *

class Cart:
    def __init__(self, total_price = 0):
        self.__items = []
        self.__total_price = total_price

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        if  self.product.price != self.product.promotion_price:
            return self.product.promotion_price * self.quantity
        else:
            return self.product.price * self.quantity

class ShoppingCart:
    def __init__(self, total = 0):
        self.items = []
        self.total = total

    def add_item(self, product, quantity=1):
        self.check_product_status(product)
        product.reduce_quantity(quantity)

        for item in self.items:
            if item.product == product:
                item.quantity += quantity
                return

        new_item = CartItem(product, quantity)
        self.items.append(new_item)

    def remove_item(self, product):
        for item in self.items:
            if item.product == product:
                self.items.remove(item)
                item.product.quantity += item.quantity
                return

    def get_total_price(self):
        for item in self.items:
            self.total += item.total_price()
        return self.total

    def check_product_status(self, product):
        if product.status != "available":
            raise Exception(f"{product.name} is not available for sale")
        
    def view_cart(self):
        item_strings = []
        for item in cart.items:
            item_string = f"{item.product.name} ({item.quantity}) - {item.total_price()}"
            item_strings.append(item_string)

        if not item_strings:
            return "Your shopping cart is empty."

        return (item_strings)
    
# Create some products
product1 = Product('Key1', 101, 20, 18, 23)
product2 = Product('Key2', 102, 10, 7, 24)
product3 = Product('Key3', 103, 80, 60, 25)

# Create a shopping cart
cart = ShoppingCart()


# Add some items to the cart
cart.add_item(product1, 2)  
cart.add_item(product2, 1)  
cart.add_item(product3, 3)  

total_price = cart.get_total_price()

print(ShoppingCart.view_cart(cart))