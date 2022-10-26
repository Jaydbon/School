# ********* Variables ************
userExit = True
runLoop = True
inValue = 0 # user inputted data
outValue = 0 # output for the user

# ************ FUNCTIONS ***************
# mph and kph
def inValid(valCheck):
    while True:
        if not valCheck:
            print("Input cannot be empty")
            return False
        else:
            try:
                float(valCheck)
                return True
            except:
                print("Invalid Input, Must be a number") # printing first giving input
                return False

def convert_MPH():  # mph - kph
    inValue = input("Please enter your miles per hour speed: ") # taking the mph
    inputValid = inValid(inValue)
    if inputValid ==True:
        outValue = float(inValue) / 0.6 # calculating the answer
        if outValue > 0:
            print("Your speed is %.2f km/h" %(outValue))
        else:
            print("Invalid input Value cannot be 0")

def convert_KPH(): # kph - mph
    inValue = input("Please enter your kilometers per hour speed: ") # taking the kph
    inputValid = inValid(inValue)
    if inputValid ==True:
        outValue = float(inValue * 0.6) # calculating the answer
        if outValue > 0:
            print("Your speed is %.2f m/h" %(outValue))
        else:
            print("Invalid input Value cannot be 0")
# cm and in
def convert_cm():  # cm - in
    inValue = input("Please enter the centimeters distance: ") # taking the cm
    inputValid = inValid(inValue)
    if inputValid ==True:
        outValue = float(inValue) / 2.54 # calculating the answer
        if outValue > 0:
            print("Your distance is %.2f in" %(outValue))
        else:
            print("Invalid input Value cannot be 0")
def convert_in():  # in - cm
    inValue = input("Please enter the inches of your distance: ") # taking the in
    inputValid = inValid(inValue)
    if inputValid ==True:
        outValue = float(inValue) * 2.54 # calculating the answer
        if outValue > 0:
            print("Your distance is %.2f cm" %(outValue))
        else:
            print("Invalid input Value cannot be 0")

# lbs and kg
def convert_lbs():  # LBS to kg
    inValue = input("Please enter the lbs of your weight: ") # taking the LBS
    inputValid = inValid(inValue)
    if inputValid ==True:
        outValue = float(inValue) * 0.45359237 # calculating the answer
        if outValue > 0:
            print("Your weight is %.2f kg" %(outValue))
        else:
            print("Invalid input Value cannot be 0")

def convert_kg():  # kg to LBS
    inValue = input("Please enter the kg of your weight: ") # taking the kg
    inputValid = inValid(inValue)
    if inputValid ==True:
        outValue = float(inValue) / 0.45359237 # calculating the answer
        if outValue > 0:
            print("Your weight is %.2f lbs" %(outValue))
        else:
            print("Invalid input Value cannot be 0")

# f and c
def convert_f():  # f to c
    inValue = input("Please enter the fahrenheit of your temperature: ") # taking the f
    inputValid = inValid(inValue)
    if inputValid ==True:
        outValue = (float(inValue) -32) / 1.8  # calculating the answer
        print("Your temperature is %.2f c" %(outValue))

def convert_c():  # c to f
    inValue = input("Please enter the celsius of your temperature: ") # taking the c
    inputValid = inValid(inValue)
    if inputValid ==True:
        outValue = (float(inValue) * 1.8) +32  # calculating the answer
        print("Your temperature is %.2f f" %(outValue)) # printing the result

    
# ******* PROGRAM *********

while runLoop == True:
    print("1. Speed 2. Distance 3. Weight 4. Temperature") 
    convertSelect = input("What would you like to convert (1, 2, 3, 4): ") # selecting which units
    inputValid = inValid(convertSelect)
    if inputValid ==True:
        if float(convertSelect) == 1: #If the user selected speed
            print("1. MPH to KPH, 2. KPH to MPH") # asking for imperial to metric or metric to imperial
            userSelect = input("What would you like to convert (1 or 2): ")
            inputValid = inValid(userSelect)
            if inputValid ==True:
                if float(userSelect) == 1:
                    convert_MPH()
                elif float(userSelect) == 2:
                    convert_KPH()
                else:
                    print("invalid entry, please try again")
                    continue
                
        elif float(convertSelect) ==2: # if the user selected distance
            print("1. CM to IN, 2. IN to CM")# asking for imperial to metric or metric to imperial
            userSelect = input("What would you like to convert (1 or 2): ")
            inputValid = inValid(userSelect)
            if inputValid ==True:
                if userSelect == 1:
                    convert_cm() # runs the function
                elif float(userSelect) == 2:
                    convert_in()
                else:
                    print("invalid entry, please try again")
                    continue
                
        elif float(convertSelect) ==3: # if the user selected weight
            print("1. LBS to KG 2. KG to LBS")# asking for imperial to metric or metric to imperial
            userSelect = input("What would you like to convert (1 or 2): ")
            inputValid = inValid(userSelect)
            if inputValid ==True:
                if float(userSelect) == 1:
                    convert_lbs()
                elif float(userSelect) == 2:
                    convert_kg()
                else:
                    print("invalid entry, please try again")
                    continue
                
        elif float(convertSelect) ==4: # if the user selected temperature
            print("1. F to C 2. C to F")# asking for imperial to metric or metric to imperial
            userSelect = input("What would you like to convert (1 or 2): ")
            inputValid = inValid(userSelect)
            if inputValid ==True:
                if float(userSelect) == 1:
                    convert_f()
                elif float(userSelect) == 2:
                    convert_c()
                else:
                    print("invalid entry, please try again")
                    continue
        else:
            print("Invalid input")
            continue
        userExit = input("Convert Another Value? (Y/N)") # asking if the user would like to continue
        if userExit.upper() != "Y": # != means not true
            break
print("Have a great day")
print("Program Exited")

    
#end
