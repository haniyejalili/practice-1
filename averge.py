name = input("please insert student name ")
family_name = input("please insert student last neme ")
grade1 = float(input(" first lesson: "))
grade2 = float(input(" second lesson: "))
grade3 = float(input(" third lesson: "))


average = (grade1 + grade2 + grade3) / 3
if (grade1,grade2)<0:
    print("error")

if average >= 17:
    print (name,"great.")
elif average >= 12<17:
    print("normal")
else:
    print("fail")
