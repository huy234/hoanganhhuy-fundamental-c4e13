print("hi dere here are your fav things so far")
fav=["death note","netflix","teaching"]
star = "* * * * * * * * * "
print(star)
for index, val in enumerate(fav):
    print(index+1 ,val, sep=". ")
print(star)
new = int(input("position you want to replace  "))
update= input("your new favourite  ")
fav[new-1] = update
for index, fav in enumerate(fav):
    print(index+1 ,fav, sep=". ")