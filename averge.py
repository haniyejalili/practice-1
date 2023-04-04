name = input("please insert stdent name ")
family_name = input("please insert student last neme ")
grade1 = float(input(" first lesson"))
grade2 = float(input(" second lesson "))
grade3 = float(input(" third lesson "))

average = (grade1 + grade2 + grade3) / 3

if average >= 17:
    print ("great.")
elif average >= 12<17:
    print("normal")
else:
    print("fail")
