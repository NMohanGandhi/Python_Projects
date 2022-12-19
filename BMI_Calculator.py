Height    =  float(input(" Enter your height in centimeters: "))
Weight   =   float(input("Enter your weight in kg:  "))
Height   = Height/100
BMI       =  Weight/(Height*Height)
print("your Body Mass Index is : ",BMI)
if BMI>0:
    print("Ready to Calculate your BMI")
    if BMI<18.5:
        print("Under Weight")
    elif (BMI>=18.5 and BMI<=24.9):
        print("Normal Weight")
    elif(BMI>=25 and BMI<=29.9):
        print("Over Weight")
    elif(BMI>=30 and BMI<=34.9):
        print("Obesity Class 1")
    elif(BMI>=35 and BMI<=39.9):
        print("Obesity Class 2")
    elif(BMI>=40):
        print("Obesity Class 3")
else:
    print("Please enter valid Height and Weight")
              
    
    
