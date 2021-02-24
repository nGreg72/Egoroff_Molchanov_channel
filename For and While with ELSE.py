from random import randint

l = [randint(1, 100) for i in range(100)]
l.sort()
print(l)

for i in l:
    if i == 20:
        print("Found! Value = ", i)
        break
else:
    print("Nothing found")
