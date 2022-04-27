class Calculator():
    def __init__(self, input1, input2): #store the 2 input variables as the class attribute
        self.input1 = input1 
        self.input2 = input2

    def adder(self):
        return self.input1 + self.input2 # add both numbers

    def subtractor(self):
        return self.input1 - self.input2 # subtract both numbers

    def multiplier(self):
        return self.input1 * self.input2 # multiply both numbers

    def divider(self):
        return round(self.input1 / self.input2,2) # divide both numbers

    def clear(self): # set both numbers to zero 
        self.input1 = 0
        self.input2 = 0        

if __name__ == "__main__":
    x = int(input("Please enter the first number: ")) # take in user input and convert it to int
    y = int(input("Please enter the second number: ")) # take in user input and convert it to int
    calc = Calculator(x, y) # creates a new calculator object called calc
    print(f"The 2 values added: {calc.adder()}") # prints the result of calling adder
    print(f"The 2 values subtracted: {calc.subtractor()}") # prints the result of calling subtractor
    print(f"The 2 values multiplied: {calc.multiplier()}") # prints the result of calling multiplier
    print(f"The 2 values divided: {calc.divider()}") #prints the result of calling divider
    calc.clear() # clears the input values then print the values of the 2 numbers
    print(f"After clearing values: \nfirst number is {calc.input1}, second number is {calc.input2}.")

