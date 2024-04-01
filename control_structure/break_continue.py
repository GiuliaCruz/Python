for x in range(1 , 11):
    if x % 2 == 0:
        continue # interrupts the repetition and moves on to the next
    print(x)

for x in range(1, 11):
    if x == 5:
        break # the control exits from the loop
    print(x)
print('End')