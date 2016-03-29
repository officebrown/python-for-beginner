# Useless Trivia
#
# Gets personal information from the user and then
# prints true but useless information about him or her

name = input('What is your name? ')
age = float(input('What is yoru age? '))
weight = float(input('How much do you weigh? '))
moon_weight = weight / 6
name_converted = name.title().strip()
age_converted = int(age)

print(name_converted + ', you are', str(age_converted), 'years old and you weigh', weight, 'lbs.')
print('On the moon, ' + name_converted + ', you\'d weigh', moon_weight, 'lbs.' )
print((name + name_converted + '\n') * 50)
input('Press "enter" to exit.')
