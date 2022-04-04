class clockTime():
    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = 0,0,0 # initialise the hours, minutes and seconds to 0
        self.setHours(hours) # calls setHours function
        self.setMinutes(minutes) # calls setMinutes function
        self.setSeconds(seconds) #calls setSeconds function

    def inputChecker(self, value, limit): #takes in value and limit
        if ((value > limit) or (type(value) != int)) or (value < 0): #checks if the value is more than limit, if the value is type int and if value is less than or equal 0
            raise ValueError # raise valueerror if doesnt meet above criteria
        return value # else return the value

    def setHours(self, hours):
        try:
            self.hours = self.inputChecker(hours, 23) # calls inputChecker to try to set hours
        except ValueError:
            print("Invalid hours entered.") # if hours invalid, catch exception and print invalid hours
            raise

    def setMinutes(self, minutes):
        try:
            self.minutes = self.inputChecker(minutes, 60) # calls inputChecker to try to set minutes
        except ValueError:
            print("Invalid minutes entered.") #if minutes invalid, catch exception and print invalid minutes
            raise

    def setSeconds(self, seconds):
        try:
            self.seconds = self.inputChecker(seconds, 60) # calls inputChecker to try to set seconds
        except ValueError:
            print("Invalid seconds entered.") # if seconds invalid, catch exception and print invalid seconds
            raise
        
    def showTime(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}") # print in formatted, hours:minutes:seconds

hours,minutes,seconds = input("Please enter hours, minutes and seconds seperated by comma: ").split(",") # take in user input and split into hours, minutes and seconds by comma
clock = clockTime(int(hours),int(minutes),int(seconds)) # creates new object clock and pass hours, int and seconds into the clockTime class
clock.showTime() # calls showTime to print the time.