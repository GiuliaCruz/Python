word = 'paralelepípedo'
for letter in word:
    print(letter, end= ',')
print('End')

approved = ['Jhonny', 'Bob', 'Billie', 'Vick']
for name in approved:
    print(name)

for position, name in enumerate(approved):
    print(position + 1, name)

days_week = ('Sunday', 'Monday', 'Tuesday',
              'Wednesday', 'Thursday', 'Friday', 'Saturday')
for day in days_week:
    print(f'Today is {day}!')

for letter in set('very nice'):
    print(letter)