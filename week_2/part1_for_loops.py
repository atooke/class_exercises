'''
Write a script that computes and prints the factorial of a user inputted number.
'''
user_input = int(input('please enter number to calculate factorial for: '))
result = 1
for i in range(user_input, 1, -1):
    result *= i
print(result)



'''
Write a script that determines whether or not a user inputted number is a prime and prints 'The number you inputted is
a prime/ not a prime number.' depending on what your script finds.
'''
user_input = int(input('Please enter number to be tested if its prime #: '))

msg = 'prime #'
for i in range(2, user_input):
    if user_input % i == 0:
        msg = 'not prime #'
print(msg)