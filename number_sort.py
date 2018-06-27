
numbers=[-10, 2, -8, 7, -142]
numb=[]
sorting = True
while sorting:
    min_numb = min(numbers)
    numb.append(min_numb)
    numbers.remove(min_numb)

    if len(numbers) == 0:
        sorting = False
print(*numb)