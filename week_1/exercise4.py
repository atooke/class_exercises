total = 0
for i in range(1, 50):
    total += i
    print(total)
    if total >= 100:
        print(i)
        break
