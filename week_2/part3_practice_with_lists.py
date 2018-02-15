'''
Write a script that creates a list of only the even numbers between 0 and a user inputted number.
'''
user_input = int(input('please enter a number: '))
result = []
for i in range(0, user_input+1):
    if i % 2 == 0 :
        result.append(i)
print(result)

'''
Write a script that creates a list of only numbers divisible by a user inputted number that are between 0 and a user 
inputted number (Hint: Use input() twice to get both of the user inputs).
'''
user_max_num = int(input('please enter a number: '))
user_div_by_num = int(input('please enter a number: '))
result = []
for i in range(1, user_max_num+1):
    if i % user_div_by_num == 0:
        result.append(i)
print(result)



'''
Given the list [0, 3, 6, 9, 10, 2, 5] and [2, 6, 4, 7, 8, 1, 15], write a script that finds the common elements between
them. Store them in a list, and print that list, sorted, as the final output (if you'd like you can go ahead and hard
code those lists in your script).
'''

list_1 = [0, 3, 6, 9, 10, 2, 5]
list_2 = [2, 6, 4, 7, 8, 1, 15]
print('In list 1 &2', set(list_1).intersection(set(list_2)))


'''
For a user inputted number, write a script that outputs a list of multiples of that number from 0 up to another user 
inputted number. For example, given the numbers 4 and 20, your script should print the numbers 4, 8, 12, and 16.'''

usr_max_num = int(input('please enter max number to calculate multiples up to: '))
user_mult_num = int(input('please enter a multiple: '))
result = []
for i in range(1,user_max_num+1):
    result.append(i * user_mult_num)
print(result)



