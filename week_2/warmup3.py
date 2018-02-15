my_list = ['hello', 'there', 'python', list('list'), '!']
for element in my_list:
    print(element)



'''
Change the code in warmup3.py so that it also prints the indices of the elements in my_list.
'''
print('*'*48)
my_list = ['hello', 'there', 'python', list('list'), '!']
for idx, element in enumerate(my_list):
    print(idx, element)


'''
add an if to the for loop so that only the elements at odd indices are printed, along with their index.
'''
print('*'*48)
my_list = ['hello', 'there', 'python', list('list'), '!']
for idx, element in enumerate(my_list):
    if idx % 2 != 0:
        print(idx, element)


'''
Change your if statement to only print the elements that are longer than 4 characters, again along with their index. 
Why can you just len() to do this?
'''
print('*'*48)
my_list = ['hello', 'there', 'python', list('list'), '!']
for idx, element in enumerate(my_list):
    if len(element) > 4:
        print(idx, element)



'''
Now, instead of just printing the elements to the console, change the script so that it adds the elements that are 
longer than 4 characters to a new list, called longer_elements. This means that you will have to create an empty list 
with that name before the list. Print longer_elements at the end of the script.

'''
print('*'*48)
longer_elements = []
my_list = ['hello', 'there', 'python', list('list'), '!']
for idx, element in enumerate(my_list):
    if len(element) > 4:
        longer_elements.append(element)
print(longer_elements)


'''
Try printing longer_elements inside the for loop you created above. What do you expect to see when you run your script?
Make sure you understand why you're getting this output.
'''
# list will print each iteration & each iteration will have n+1 more words



'''
Add the line user_number = int(input('Min length to be printed: ')) to the top of warmup3.py. Now, change your script 
so that it only adds words that are longer than a user inputted number to longer_elements. You can include the statement
 printing longer_elements inside the loop if you want. Print longer_elements after the loop.
'''
user_number = int(input('Min length to be printed: '))
print('*'*48)
longer_elements = []
my_list = ['hello', 'there', 'python', list('list'), '!']
for idx, element in enumerate(my_list):
    if len(element) > user_number:
        longer_elements.append(element)
print(longer_elements)












