my_list = [1, 'hello', 2, 'there', 3, 'list']
print(my_list[1])


#Q1 - List index starts @ 0 not 1 so above line will print 'hello'
print(my_list[0])


'''
#Q2 - Now change the print statement so that only the words "hello", "there", and "list" are grabbed from my_list 
and printed. You should do this with indexing. What do you expect the type of the thing that is printed to be?
'''
print(my_list[1::2])

'''
Put a line between lines 1 and 2 that adds the number 4 to the end of my_list.
'''
my_list = [1, 'hello', 2, 'there', 3, 'list']
my_list.append(4)
print(my_list)


'''
Change the print statement so that only the numbers in my_list are printed. Again, do this with indexing.
'''
print(my_list[::2])



'''
Add another line after the one with append() that removes the word "list" from my_list. What do you think my_list 
looks like now? Print it to check.
my_list = [1, 'hello', 2, 'there', 3, 'list']
my_list.append(4)
print(my_list)
'''
my_list = [1, 'hello', 2, 'there', 3, 'list']
my_list.append(4)
my_list.remove('list')
print(my_list)


'''
Now, using indexing, print only the elements in my_list at odd indices. You should see: ['hello', 'there', 4] 
Is this what you'd expect? If not, consider how you've transformed my_list, and convince yourself that this makes sense.
'''
print(my_list[1::2])



'''
Remove the lines that modify my_list. Now add the line user_input = input('Add the number 4 to mylist (y/n)? ') at the 
top of warmup2.py. Modify the rest of warmup2.py so that if the user inputs a y, it will add the number 4 to the end of
 my_list, and otherwise it will do nothing. At the end, print my_list. Play around with different inputs. Do they work 
the way you'd expect?
'''


user_input = input('Add the number 4 to mylist (y/n)? ')
my_list = [1, 'hello', 2, 'there', 3, 'list']
if user_input.lower() == 'y':
    my_list.append(4)
print(my_list)

'''
Modify warmup2.py so that it will accept any user inputted string. If the length of that string is less than 8, your 
script should add it to my_list, and other wise it should add the number 4 to the list. Print my_list at the end to 
see what it is.
'''


user_input = input('enter any string: ')
if len(user_input) < 8:
    my_list.append(user_input)
else:
    my_list.append(4)
print(my_list)

