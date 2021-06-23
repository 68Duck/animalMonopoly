def getIntegerInput(inputMessage):
    valid = False
    while not valid:
        inp = input(inputMessage)
        try:
            inp = int(inp)
            valid = True
        except:
            print("The input is not valid. Please try again")
    return inp

def getPositiveIntegerInput(inputMessage): #does include 0
    valid = False
    while not valid:
        inp = input(inputMessage)
        try:
            inp = int(inp)
            if inp < 0:
                print("The number is less than 0. Please try again")
            else:
                valid = True
        except:
            print("The input is not valid. Please try again")
    return inp

def getNonZeroPositiveIntegerInput(inputMessage):
    valid = False
    while not valid:
        inp = input(inputMessage)
        try:
            inp = int(inp)
            if inp <= 0:
                print("The number is not positive. Please try again")
            else:
                valid = True
        except:
            print("The input is not valid. Please try again")
    return inp


def getAnyInput(inputMessage):
    valid = False
    while not valid:
        inp = input(inputMessage)
        if not inp:
            print("The input needs to not be blank. Please try again.")
        else:
            valid = True
    return inp

def getGreaterThanInput(inputMessage,greaterThanValue):
    valid = False
    while not valid:
        inp = input(inputMessage)
        try:
            inp = int(inp)
            if inp<=greaterThanValue:
                print(f"The input needs to be greater than {greaterThanValue}.\nPlease try again")
            else:
                valid = True
        except:
            print("The input is not valid. Please try again")
    return inp


def runTestInputs():
    # inp = getIntegerInput("Give me an integer")
    # print(f"The input is {inp}")
    # inp = getPositiveIntegerInput("Give me an integer")
    # print(f"The input is {inp}")
    # inp = getNonZeroPositiveIntegerInput("Give me an integer")
    # print(f"The input is {inp}")
    # inp = getAnyInput("Give me an integer")
    # print(f"The input is {inp}")
    inp = getGreaterThanInput("Give me an integer",10)
    print(f"The input is {inp}")

if __name__ == "__main__":
    runTestInputs()
