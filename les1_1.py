# first point of practical task for first lesson "Basic Python"
a = 10
b = 5.5
c = 'Some text'
d = True

print(a, b, c, d)

first_number = input('Enter some integer please\n>>>')
second_number = input('Enter some float please\n>>>')
if first_number.isdigit():
    print('The sum of your integer and variable "a" =', a + first_number)
else:
    print('You have entered not a digit! Please enter an integer!')

user_name = input('Please enter your name\n>>>')
user_city = input('Please enter city where you was born\n>>>')
print(f'Dear, {user_name} you were born in {user_city} - the greate city!')

