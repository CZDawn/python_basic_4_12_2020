user_name = input('Let\'s get to know you. What\'s your name?\n>>>')
computer_greeting = f'Hello! Nice to meet you {user_name}!'
print(computer_greeting)

user_age = input('Please tell me how old are you?')
if user_age.isdigit():
    print('It\'s greate age to become an a programmer!')
else:
    print('Be shure that you enter an integer!')

