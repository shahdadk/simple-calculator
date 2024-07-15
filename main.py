
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
    
    
# Input 1 While Loop
while True:
    input1 = input("Hi what would you like the first number to be?")
    try:
        input1=float(input1)
        break
    except ValueError:
        print("Not a valid number, please try again!")
        continue

# Input 2 While Loop
while True:
    input2 = input("What would you like your second number to be?")
    try:
        input2=float(input2)
        break
    except ValueError:
        print("Not a valid number, do you know what a number is?")
        continue

instance1 = Calculate(input1, input2)

#main calculator loop
while True:
    input3= input("What operation would you like to dooooo? 1 - Addition, 2 - Subtraction, 3 - Multiplication, 4 - Division, 5 - Quit")

    if input3 == "1":
        print(str(instance1.addition(input1, input2)))
        continue
    elif input3=="2":
        print(str(instance1.subtraction(input1, input2)))
        continue
    elif input3=="3":
        print(str(instance1.multiplication(input1, input2)))
        continue
    elif input3=="4":
        print(str(instance1.division(input1, input2)))
        continue
    elif input3=="5":
        print("Ok thanks for using our calculator")
        break
    else:
        print("Not a valid input, please try again.")
        continue
