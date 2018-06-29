shopping=True
clothes=["T-Shirt","Sweater"]
print("Hello and welcome to my Shop")
print("Here's what we have: ",*clothes,sep=" ")
ans = input("What do you want?(C,R,U,D)"   )
while shopping:
    if ans == "C":
        new = input("what do you want to add?  ")
        clothes.append(new)
        print(*clothes)
    elif ans == "R":
        print(*clothes)
    elif ans == "U":
        pos = int(input("Position you want to replace"))
        update=input("What do you want to replace?  ")
        clothes[pos-1]= update
        print(*clothes)
    elif ans == "D":
        place = int(input("Position you want to delete?  "))
        del clothes[place-1]
        print(*clothes)
    else:
        shopping = False



