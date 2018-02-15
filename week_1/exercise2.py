

nums = [1, 2, 3, 4, 6, 9, 10]
for i in nums:
    if i % 2 == 0:
        if i % 3 == 0:
            print('even and divisble by 3')
        else:
            print('even')
    else:
        if i % 3 == 0:
            print('odd and divisble by 3')
        else:
            print('odd')
