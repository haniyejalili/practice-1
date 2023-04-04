h = float(input("enter yor height in meter"))
w = float(input("enter your weight in kilogram"))
bmi = (w/(h * h))
if bmi < 18.5: 
   print ("you are under wight") 
elif bmi  >= 18.5 and bmi<25:
   print ('you are normal weight')
elif bmi >=25 and bmi<30:
   print ("you are over wight")
else:
   print("you are fat")
if w<0 or h<0:
   print("error")
 