name = input("please insert student name ")
family_name = input("please insert student last neme ")
grade1 = float(input(" first lesson: "))
grade2 = float(input(" second lesson: "))
grade3 = float(input(" third lesson: "))
print (name)
print (family_name)

average = (grade1 + grade2 + grade3) / 3
if grade1 >20:
    print("error number 1")
if grade2 >20:
    print("error number 2")
if grade3 >20:
    print("error number 3")

if average >= 17:
    print ("great.")
elif average >= 12<17:
    print("normal")
else:
    print("fail")
