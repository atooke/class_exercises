x = [1, 9, 10, 99, 100, 2, 80, -11]
for i in x:
    if i % 2 == 0:
        print("x=", i, 'This the best number')
    elif i < 10:
        print("x=", i, 'This is a good number.')
    elif i > 9 and i < 99:
        print("x=", i, "This is a better number.")
    else:
        print("x=", i, "horrible number")