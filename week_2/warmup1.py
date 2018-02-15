my_str = "This String wasn't Chosen Arbitrarily..."
my_str = my_str + "oR wAs it??"

print(my_str.upper())

print(my_str[14:15])
print(my_str.lower())
print(my_str[40:])
print(my_str[40:51].upper())



my_str = "This String wasn't Chosen Arbitrarily..."
my_str_2 = "oR wAs it??"
user_input = input('Add "oR wAs it??" (y/n)? ')
if user_input.lower() == 'y':
    print(my_str + my_str_2)
else:
    print(my_str)


my_str = "This String wasn't Chosen Arbitrarily..."
user_input = input('String to add to end of my_str: ')
print(my_str + user_input)




my_str = "This String wasn't Chosen Arbitrarily..."
user_input = input('String to add to end of my_str: ')
if len(user_input) < 10:
    print(my_str + user_input)
else:
    print(user_input)