NOT_DIGIT = 'Be shure that you entered an integer!'

user_name = input('Let\'s get to know you. What\'s your name?\n>>>')
system_message = f'Hello! Nice to meet you {user_name}!'
print(system_message)

user_age = input('How old are you?\n>>>')
if user_age.isdigit():
    print('It\'s greate age to become an a programmer!')
else:
    print(NOT_DIGIT)

time_to_convert = input('Enter the time in seconds so I can convert it in Hours:Minutes:Seconds.\n>>>')
if time_to_convert.isdigit():
    hours = int(time_to_convert) // 3600
    minutes = int(time_to_convert) % 3600 // 60
    seconds = int(time_to_convert) % 3600 % 60
    print(hours, ':', minutes, ':', seconds)
else:
    print(NOT_DIGIT)

some_number = input('Let\'s count next example: n+nn+nnn. Enter an arbitrary number.\n>>>')
n = some_number
nn  = some_number + some_number
nnn = some_number + some_number + some_number
if n.isdigit() and nn.isdigit() and nnn.isdigit():
    count = int(n) + int(nn) + int(nnn)
    system_message = f'The result is {count}.'
    print(system_message)
else:
    print(NOT_DIGIT)

number = input('Enter some number')
large_number = ''
i = 0
while i < len(number):
    if number[i] < number[i-1]:
        i = i + 1
        continue
    else:
        large_number = number[i]
print(large_number)

revenue_value = input('Enter the income value wich your firm have earned in last year, in rubles.\n>>>')
costs_value = input('Enter the costs value wich your firm have spend in last year, in rubles.\n>>>')
if revenue_value.isdigit() and costs_value.isdigit():
    revenue_value = int(revenue_value)
    costs_value = int(costs_value)
    if revenue_value > costs_value:
        profit_value = revenue_value - costs_value
        profitability = profit_value / revenue_value * 100
        system_message = f'Your\'s firm had profit in last year, the value of profit was - {profit_value} rubles.\n Profitability of the firms revenue is {profitability}%.'
        print(system_message)
    elif revenue_value < costs_value:
        loss_value = costs_value - revenue_value
        system_message = f'In last year your firm suffered losses in value - {loss_value} rubles. You have to find the way to make up for losses.'
        print(system_message)
    else:
        system_message = 'Your firm  didn\'t yearn money last year, the revenue and costs was equal. You shoud change some to become profitable.'
        print(system_message)
else:
    print(NOT_DIGIT)

