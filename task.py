# getting input from the user and assigning it to user
import json
json_data='{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }'
                                                                         
python_obj=json.loads(json_data)


cm = python_obj['HeightCm']
height=cm / 100.0; 
weight = python_obj['WeightKg']


bmi = weight/height 




print("Your BMI is: {0} and you are in: ".format(bmi), end='')

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

