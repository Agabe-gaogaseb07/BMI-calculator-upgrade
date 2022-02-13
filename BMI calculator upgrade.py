
#Prompts the needed details with the float and the input function.
#The float rounds all decimals to a whole number.

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg?: "))

#Calculates the Body Mass Index using the weight and height entered to the power of 2.
BMI = round(float(int(weight) / int(height**2)))

#Using the f-string it will print out what is your Body Mass Index(BMI) using the If statement.
if BMI <18.5:
    print(f"Your BMI is {BMI}, Your are underweight")
    
if BMI >18.5 and BMI <= 25:
    print(f"Your BMI is {BMI}, You are Normal Weight")
    
if BMI >25 and BMI<30:
    print(f"Your BMI is {BMI}, You are Overweight")
 
if BMI >30 and BMI <35:
    print(f"Your BMI is {BMI}, You are Obese")
if BMI >=35:
    print(f"Your BMI is {BMI}, You are Clinically Obese")
