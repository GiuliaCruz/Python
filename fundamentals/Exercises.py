#exercise 1
number = 16

if(number%2==0):
    answer = "the number is even"
else:
    answer = "the number is odd"

print(answer)

#exercise 2
average = 8.5

if(average>=7.0):
    answer = "approved"
elif(average>=5.0): #else + if
    answer = "retake test"
else: #less than 5.0
    answer = "reproved"

print(answer)

#exercise 3
unit_value = 10.00
discount10 = 0.1 #10%
discount20 = 0.2 #20%
amount = eval(input("Enter the quantity you will purchase: "))
if(amount <= 10):
    final_value = unit_value*amount
elif(amount <= 20):
    final_value = unit_value*amount*(1-discount10)
else: 
    final_value = unit_value*amount*(1-discount20)

print(final_value)

#exercise 4

list =[10, 2, 5, 7, 6, 3]
sum = 0
for num in list:
    if(num%2==0):
        sum=sum+num
print(sum)