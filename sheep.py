print("")
print("Lession 3")
print("")
sheep = [15, 37, 20, 900, 100]
print("Hello my name is Hiep and these are my sheep size")
print(sheep)


sheep_max= max(sheep)
print("My biggest sheep is", sheep_max)
print("Let's sheer it!")
max_index = sheep.index(sheep_max)


sheep[max_index]=8
print("After shearing this is my flock:")
#print (max_index)
print (sheep)

for x in range(len(sheep)):
    #print (x, " = ", sheep[x])
    sheep[x] = sheep[x] + 50
    #print (x, " == ", sheep[x])
    
print("One month has passed here is my flock")
print (sheep)

print("")
print("Lession 4")
print("")
sheep = [15, 37, 20, 900, 100, 240, 547, 79]
print("Hello my name is Hiep and these are my sheep size")
print(sheep)
for i in range (3):
    print("")
    print ("Month",i+1 )
    for x in range(len(sheep)):
        sheep[x] = sheep[x] +50
    print("One month has passed here is my flock")
    print(sheep)
    sheep_max = max(sheep)
    print ("My biggest sheep is", sheep_max)
    print ("Let's sheer it!")
    max_index = sheep.index(sheep_max)
    sheep[max_index]=8
    print("After shearing this is my flock:")
    #print (max_index)
    print (sheep)
print("")
sumsheep = 0
for p in range (len(sheep)):
    sumsheep= sumsheep + sheep[p]
print("Here is my size total")
print(sumsheep)
print("I will get:  ", sumsheep*2,"$")