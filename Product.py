class Product:
    def __init__(self, name, product_id, price, promotion_price, overview, quantity, status = "available"):
        self._name = name
        self._product_id = product_id
        self._price = price
        self._promotion_price = promotion_price
        self._overview = overview
        self._quantity = quantity
        self._status = status
        self._review = []

    def reduce_quantity(self, quantity):
        if self._quantity < quantity:
            raise Exception(f"Insufficient quantity of {self.name}")
        self._quantity -= quantity

    @property
    def name(self):
        return self._name
    
    @property
    def quantity(self):
        return self._quantity

    @property
    def price(self):
        return self._price
    
    @property
    def promotion_price(self):
        return self._promotion_price

    @property
    def status(self):
        return self._status
    
    @property
    def overview(self):
        return self._overview

class Keyboard(Product):
    def __init__(self, name, product_id, price, promotion_price, overview, quantity, keyboard_switch, keyboard_keycap, keys, casecolor, status="available"):
        super().__init__(name, product_id, price, promotion_price, overview, quantity, status)
        self.__keyboard_keycap = keyboard_keycap
        self.__keyboard_switch = keyboard_switch
        self.__keys = keys
        self.__casecolor = casecolor

    @property
    def keyboard_keycap(self):
        return self.__keyboard_keycap
    
    @property
    def keyboard_switch(self):
        return self.__keyboard_switch
    
    @property
    def keys(self):
        return self.__keys
    
    @property
    def casecolor(self):
        return self.__casecolor

class Switch(Product):
    def __init__(self, name, product_id, price, promotion_price, overview, quantity, variation, spring_weight, type_switch, status="available"):
        super().__init__(name, product_id, price, promotion_price, overview, quantity, status)
        self.__variation = variation
        self.__spring_weight = spring_weight
        self.__type_switch = type_switch

    @property
    def variation(self):
        return self.__variation
    
    @property
    def spring_weight(self):
        return self.__variation
    
    @property
    def type_switch(self):
        return self.__type_switch
class Keycap(Product):
    def __init__(self, name, product_id, price, promotion_price, overview, quantity, kit, profile, type_keycap, status="available"):
        super().__init__(name, product_id, price, promotion_price, overview, quantity, status)
        self.__kit = kit
        self.__profile = profile
        self.__type_keycap = type_keycap

    @property
    def kit(self):
        return self.__kit
    
    @property
    def profile(self):
        return self.__profile
    
    @property
    def type_keycap(self):
        return self.__type_keycap