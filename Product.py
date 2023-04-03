import Review
class Product:
    def __init__(self, name, product_id, price, promotion_price, overview, quantity, status = "available"):
        self._name = name
        self._product_id = product_id
        self._price = price
        self._promotion_price = promotion_price
        self._overview = overview
        self._quantity = quantity
        self.__status = status
        self.__reviews = []

    @property
    def reviews(self):
        return self.__reviews
    @reviews.setter
    def set_review(self,reviews):
        self.__reviews = reviews
        return self.__reviews
    
    def add_review(self, rating, comment):
        new_review = Review(rating,comment)
        self.reviews.append(new_review)

    def remove_review(self,reviews):
        self.reviews.remove(reviews)

    def average_rating(self):
        if len(self.reviews) == 0:
            return 0
        else:
            total_rating = sum(review.rating for review in self.reviews)
            return total_rating/len(self.reviews)

class Keyboard(Product):
    def __init__(self, name, product_id, price, promotion_price, overview, quantity, keyboard_switch, keyboard_keycap, keys, casecolor, status="available"):
        super().__init__(name, product_id, price, promotion_price, overview, quantity, status)
        self.__keyboard_keycap = keyboard_keycap
        self.__keyboard_switch = keyboard_switch
        self.__keys = keys
        self.__casecolor = casecolor

class Switch(Product):
    def __init__(self, name, product_id, price, promotion_price, overview, quantity, variation, spring_weight, type_switch, status="available"):
        super().__init__(name, product_id, price, promotion_price, overview, quantity, status)
        self.__variation = variation
        self.__spring_weight = spring_weight
        self.__type_switch = type_switch

class Keycap(Product):
    def __init__(self, name, product_id, price, promotion_price, overview, quantity, kit, profile, type_keycap, status="available"):
        super().__init__(name, product_id, price, promotion_price, overview, quantity, status)
        self.__kit = kit
        self.__profile = profile
        self.__type_keycap = type_keycap