NOT_DIGIT = 'Be shure that you entered an integer!'

# 1 item of the task
user_name = input('Let\'s get to know you. What\'s your name?\n>>>')
system_message = f'Hello! Nice to meet you {user_name}!'
print(system_message)

user_age = input('How old are you?\n>>>')
if user_age.isdigit():
    print('It\'s greate age to become an a programmer!')
else:
    print(NOT_DIGIT)

# 2 item of the task
time_to_convert = input('Enter the time in seconds so I can convert it in Hours:Minutes:Seconds.\n>>>')
if time_to_convert.isdigit():
    hours = int(time_to_convert) // 3600
    minutes = int(time_to_convert) % 3600 // 60
    seconds = int(time_to_convert) % 3600 % 60
    print(hours, ':', minutes, ':', seconds)
else:
    print(NOT_DIGIT)

# 3 item of the task
some_number = input('Let\'s count next example: n+nn+nnn. Enter an arbitrary number.\n>>>')
n = some_number
nn = some_number + some_number
nnn = some_number + some_number + some_number
if n.isdigit() and nn.isdigit() and nnn.isdigit():
    count = int(n) + int(nn) + int(nnn)
    system_message = f'The result is {count}.'
    print(system_message)
else:
    print(NOT_DIGIT)

# 4 item of the task
positive_integer = input('Enter some positive integer, and I\'ll find the largest one digit!\n>>>')
large_digit = 0
if positive_integer.isdigit():
    positive_integer = int(positive_integer)
    while positive_integer > 0:
        residual = positive_integer % 10
        if residual > large_digit:
            large_digit = residual
        positive_integer = int(positive_integer / 10)
else:
    print(NOT_DIGIT)
print(f'The largest number is {large_digit}.')

# 5 item of the task
revenue_value = input('Enter the income value wich your firm have earned, in rubles.\n>>>')
costs_value = input('Enter the costs value wich your firm have spend, in rubles.\n>>>')
if revenue_value.isdigit() and costs_value.isdigit():
    revenue_value = int(revenue_value)
    costs_value = int(costs_value)
    if revenue_value > costs_value:
        profit_value = revenue_value - costs_value
        profitability = round(profit_value / revenue_value * 100, 2)
        system_message = f'Profitability of the revenue is {profitability}%.'
        print(f'Your\'s firm had profit in last year  - {profit_value}rubles.\n', system_message)
    elif revenue_value < costs_value:
        loss_value = costs_value - revenue_value
        system_message = f'In last year your firm suffered losses in value - {loss_value} rubles.'
        print(system_message)
    else:
        system_message = 'The revenue and costs was equal. You shoud change some to become profitable.'
        print(system_message)
else:
    print(NOT_DIGIT)

# 6 item of thq task
a = input('Enter the number of kilometers that you have done the first day of training.\n>>>')
b = input('Enter the number of kilometers that you want to handle with per day.\n>>>')
day_number = 1
if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    while a < b:
        a += a * 10 / 100
        day_number += 1
        if a > b:
            break
print(f'You will achieve the goal of more than {b} kilometers per day at {day_number} days')

