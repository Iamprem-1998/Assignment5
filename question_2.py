class calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return self.num1+self.num2
    

    def substract(self):
        return self.num2-self.num1

    def multiply(self):
        return self.num1*self.num2

    def division(self):
        return self.num2/self.num1
    
   

    
obj=calculator(10,94)
print(obj.add())
print(obj.substract())
print(obj.multiply())
print(obj.division())