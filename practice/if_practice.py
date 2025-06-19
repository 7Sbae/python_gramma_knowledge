# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bow':
#         print(car.upper())
#     else:
#         print(car.title())

# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# # answer = 17
# answer=int(input('What is the answer to the ultimate question of life, the universe, and everything?'))
# if answer!=42:
#     print('That is not the correct answer. Please try again')
# else:
#     print('Correct')

# age_0 = 22
# age_1 = 18
# age_2 = 21
# age_0>=21 and age_1 >=21
# age_1 = 22
# age_0>=21 and age_1 >=21

# age_0 = 22
# age_1 = 18
# age_2 = 21
# age_0>=21 or age_1 >=21
# age_0 = 18
# print(age_0>= 21 or age_1 >=21)

# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'

# if user not in banned_users:
#     print(f'{user.tittle()},you can post a response if you wish')

# car='subaru'
# car=input('What is your favorite car:')
# if car == 'subaru':
#     print('Is car == subaru? I predict True')
#     print(car.title())
# else:
#     print('Is car == subaru? I predict False')
#     print(car.title())

# age =int(input('How old are you:'))
# if age>= 18:
#     print('You are old enough to vote!')
#     print('Have you registered to vote yet?')
# elif age < 18:
#     print('Sorry, you are too young to vote.')
#     print('Please register to vote as soon as you turn 18!')

# age =int(input('How old are you:'))
# if age < 4:
#     print('Your admission cost is $0.')
# elif age <18:
#     print('Your admission cost is $5.')    
# else:
#     print('Your admission cost is $10.')

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >= 65:
#     price = 5
# print(f'Your admission cost is ${price}.')

# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print('Adding mushrooms.')
#     if 'pepperonis' in requested_toppings:
#         print('Adding pepperonis.')
#         if 'extra cheese' in requested_toppings:
#             print('Adding extra cheese.')
# else:
#     if 'pepperonis' in requested_toppings:
#         print('Adding pepperonis.')
#         if 'extra cheese' in requested_toppings:
#             print('Adding extra cheese.')
#         else:
#             print('\nFinished making your pizza!')    

# requested_topping =input('What topping would you like on your pizza?')
# requested_toppings = ['mushrooms', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in requested_toppings:
#         print(f'Adding {requested_topping}.')
#     else:
#         print(f'Sorry, we are out of {requested_topping}.')
# print('\nFinished making your pizza!')

# requested_toppings = []
# requested_toppings.append(input('What topping would you like on your pizza:'))
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f'Adding {requested_topping}.')
#     print('\nFinished making your pizza!')
# else:
#     print('Are you sure you want a plain pizza?')

# number =list(range(1,10))
# for number in number:
#     if number == 1:
#         ordinal_suffix = 'st'
#     elif number == 2:
#         ordinal_suffix = 'nd'
#     elif number == 3:
#         ordinal_suffix = 'rd'
#     else:
#         ordinal_suffix = 'th'
#     print(str(number)+ordinal_suffix)

current_users = ['Alice', 'Bob', 'charlie', 'Aavid', 'eve']
current_users = [user.lower() for user in current_users]
new_users = ['Frank', 'George', 'Hannah', 'Alice', 'Bob']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'Sorry, {new_user} is already taken. Please choose a different username.')
    else:
        print(f'Welcome, {new_user}!')


















