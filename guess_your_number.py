low = 0
high = 100
playing=True
while playing:
    mid= (low+high) // 2
    ans = input ("is {0} your number:  ".format(mid)).upper()
    if ans == "C":
        print("i knew it!")
        break
    elif ans == "S":
        low = mid
    elif ans == "L":
        high = mid
    else:
        playing = False