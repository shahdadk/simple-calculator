
#class calculator
class Calculate:

    def __init__(self):
        pass

    def addition(self, input1, input2):
        sum = input1 + input2
        return sum
    
    def subtraction(self, input1, input2):
        difference = input1 - input2
        return difference
    
    def multiplication(self, input1, input2):
        product = input1 * input2
        return product
    
    def division(self, input1, input2):
        if input2 == 0:
            if input1 / input1 == 1:
                return "infinity"
            else:
                return "-infinity"

    def addEntry(self, entry, expression):
        expression += entry
        return expression

    def clearEntry(self, expression):
        expession = expression[:-1]
        print(expression)
        return expression
    
    def allClear(self, expression):
        expression=""
        return expression
    
    def calculateExpression(self, expression):
        
        return result
    

    
    
# Input 1 While Loop
while True:
    input1 = input("Hi what would you like the first number to be?")
    try:
        input1 = float(input1)
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

instance1 = Calculate()

#main calculator loop
while True:
    input3= input("What operation would you like to dooooo? 1 - Addition, 2 - Subtraction, 3 - Multiplication, 4 - Division, 5 - New Inputs , 6 - Quit")

    if input3 == "1":
        print(str(instance1.addition(input1, input2)))
        continue
    elif input3 == "2":
        print(str(instance1.subtraction(input1, input2)))
        continue
    elif input3 == "3":
        print(str(instance1.multiplication(input1, input2)))
        continue
    elif input3 == "4":
        print(str(instance1.division(input1, input2)))
        continue
    elif input3 == "5":
        while True:
            input1 = input("Hi what would you like the first number to be?")
            try:
                input1 = float(input1)
                break
            except ValueError:
                print("Not a valid number, please try again!")
                continue

        #Input 2 While Loop
        while True:
            input2 = input("What would you like your second number to be?")
            try:
                input2 = float(input2)
                break
            except ValueError:
                print("Not a valid number, do you know what a number is?")
                continue
        instance1 = Calculate(input1, input2)
    elif input3 == "6":
        print("Ok thanks for using our calculator")
        break
    else:
        print("Not a valid input, please try again.")
        continue
