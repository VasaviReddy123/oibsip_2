h= float(input("enter your height in meters: "))
w= float(input("enter your weight in kilgrams: "))
if h <= 3 and w< 150:
    bmi = round(w/h ** 2)
    if bmi < 18.5:
        print(f"your bodymassindex is {bmi}, you are  underweight.")
    elif bmi < 25:
        print(f"Your bodymassindex is {bmi}, you are normal.")
    elif bmi < 30:
        print(f"Your bodymassindex is {bmi}, you are overweight.")
    elif bmi < 35:
        print(f"Your bodymassindex is {bmi}, you are Obese.")
    else:
        print(f"Your bodymassindex is {bmi}, you are clinically obese.")
else:
    print("give the input in reasonable range")