# getting input from the user and assigning it to user

cm = float(input("Enter height in cm: "))
height=cm / 100.0; 
weight = float(input("Enter weight in kg: "))


bmi = weight/height 




print("Your BMI is: {0} and you are: ".format(bmi), end='')

#conditions
if ( bmi < 18.4):
   print("Malnutrition risk")

elif ( bmi >= 18.5 and bmi < 24.9):
   print("Low risk")

elif ( bmi >= 25 and bmi < 29.9):
   print("Enhanced risk ")

elif ( bmi >= 35 and bmi < 39.9):
   print("Medium risk")

elif ( bmi >=40):
   print("High risk")

    