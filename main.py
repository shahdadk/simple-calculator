
#class calculator
class Calculate:

    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def addition(self, input1, input2):
        return self.input1 + self.input2
    
    def subtraction(self, input1, input2):
        return self.input1 - self.input2
    
    def multiplication(self, input1, input2):
        return self.input1 * self.input2
    
    def division(self, input1, input2):
        
        if self.input2 == 0:
            return "Sorry, you can't divide by zero."
        else:
            return self.input1 / self.input2
        
x=0

while x==0:
    
    while True:
        input1 = input("Hi what would you like the first number to be?")
        try:
            input1=float(input1)
            is_number = True
        except ValueError:
            is_number= False


    while True:
        input2 = input("What would you like your second number to be?")


