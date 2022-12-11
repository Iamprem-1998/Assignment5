


class Account():
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
        
          

class Savingaccount(Account):
        def __init__(self,title=None,balance=0,intrestrate=0):
            super().__init__(title,balance)
            self.intrestrate=intrestrate

obj1=Account("Akash",5000)
obj2=Savingaccount("Akash",5000,5)
print(obj2.title)
print(obj2.balance)
print(obj2.intrestrate)