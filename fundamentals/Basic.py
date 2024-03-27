print('You are ' + 3 * 'very ' + 'nice!' )
print([1, 2, 3]) #list
print({'name': 'Pedro', 'age' : 22 }) #dictionary
print(None)
print(True) #boolean
print(False) #boolean
print(1.2 + 1) #float

a = 10
b = 5.2

print(a + b)
a = 'Hello'
print(a)

x, y = 2, 5
print(x, y)

numbers = ([10, 20, 30])
print(sum(numbers))

a=['10'] #string
b=['20']
c=['30']
r= a*2 + b *3 + c*4
print(f'r={r}')

#challenge I
#f(x) = ax+b
#x = -b/a != 0
a=10
b=5
x=-b/a
print(format(x))

#challenge II
'''weight = eval(input('Enter with your weight: '))
height = eval(input('Enter with your height: '))
imc = weight/(height**2)
print('imc = ', imc)'''

hour = 15
minutes = 18
seconds = 30
print(f'{hour} : {minutes} : {seconds}')

str = 'Hello World'
print(str[0:3])