from Account import *

class Accountlist:
    def __init__(self):
        self.Account_list=[]
        
    def add_account(self, account):
        self.Account_list.append(account)
        
    def create_account(self,username,password,check_password,email, name):
        if(self.__check_correct(username)):
            if(password == check_password):
                self.Account_list.append(Customer(username,password,email,name))
                print("register successfully!!")
            else:
                print("plese check your password again!!")
        else:
            print("username had been use!!")
        
    def __check_correct(self, username):
        for account in self.Account_list:
            if account.username == username:
                return False
            else:
                return True
    
    def login(self,username,password):
        for account in self.Account_list:
            if username == account.username and password == account.password:
                if account.id == "admin":
                    return print("HI ADMIN!!!")
                else:
                    return print("welcome everyone let's shoppinggggg")
        return print("please try again!!!")

# account_list = Accountlist()

# jack = Customer("jkj", "1234", "akeraanucha1@gmail.com", "Jack")
# tai = Customer("tai", "4321", "taitai@gmail.com", "Tai")
# poon = Admin("poon", "555", "poonpoon@gmail.com", "Poon")

# account_list.add_account(jack)
# account_list.add_account(tai)
# account_list.add_account(poon)

# account_list.login("poon","555")

# account_list.login("poon","554")

# account_list.login("jkj","1234")

# account_list.create_account("jkj","444","444","chomchom@gmail.com", "Chompoo")

# account_list.create_account("chom","555","444","chomchom@gmail.com", "Chompoo")

# account_list.create_account("chom","444","444","chomchom@gmail.com", "Chompoo")