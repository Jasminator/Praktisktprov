#Author: Jasmin Velagic-Ramadani
#Date: 2024-09-25


tal_input = input('Vilka tal vill du beräkna? ')

split_list = tal_input.split(' ')
numbers_list =[]
for i in split_list:
    for x in range(10):
        multi = int(i) * (x + 1)
        numbers_list.append(f"{x} * {x + 1} = {multi}")

amount = len(split_list)

for y in range(amount * 10):
    print(numbers_list[y])


