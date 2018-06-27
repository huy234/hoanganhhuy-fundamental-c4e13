yob =int(input("Your year of birth?   "))
age= 2018 - yob # process
if age <10:
    print("Baby")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
print("your age:",age) # output