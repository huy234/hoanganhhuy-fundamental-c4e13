print("Part A")
for x in range(1, 11):
    #x = 1 => string = * 
    #x = 2 => string = * * 
    string = x * "* "
    print(string)         
print("")

print("Part B")
for y in range(10,0,-1):
    string = y * "  " + (11 - y) * "* "
    print(string)
print("")

print("Part C")
for y in range(11,0,-1):
    if y == 1:
        string = "* " * 11
    elif y == 11:
        string = "* " * 11
    else:
        string = "  "* (y-1) + "* "
    print(string)
print("")