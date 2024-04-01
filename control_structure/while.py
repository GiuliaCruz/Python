#while True: #always running
#   print('will take much timeeee')

from random import randint #random number

reveled_number = -1
secret_number = randint(0, 9)

while reveled_number != secret_number:
    reveled_number = int(input('Enter the number: '))
print('The secret number {} was found.'.format(secret_number))

# while = indeterminate amount of repetition