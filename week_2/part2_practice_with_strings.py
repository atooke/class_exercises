#question 1
user_text = input('Please enter sentance: ').lower()
user_letter = input('Please enter letter to count:').lower()
print('count= ', user_text.count(user_letter))


#Question 2
user_input = input('Please enter text: ')
if user_input.endswith('!'):
    print(user_input.upper())
else:
    print(user_input.lower())


#3
user_input = input('Please enter text: ')
for vowel in 'aeiou':
    user_input = user_input.replace(vowel, '')
print(user_input)



#4
user_input = input('Please enter text: ')
result = []
for idx, letter in enumerate(user_input):
    if idx % 2 == 0 :
        result.append(letter.upper())
    else:
        result.append(letter)
print(''.join(result))

