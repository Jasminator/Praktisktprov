#Author: Jasmin Velagic-Ramadani
#Date: 2024-09-25


tal_input = input('Vilka tal vill du beräkna? ')

# Programmet stänger av sig själv om du inte matar in en siffra
if tal_input == '':
    print('Du måste skriva en siffra, Starta om progammet')
    quit()

split_list = tal_input.split(' ')
numbers_list =[]
for i in split_list:
    for x in range(10):
        multi = int(i) * (x + 1)
        numbers_list.append(f"{i} * {x + 1} = {multi}") # Variablerna är rätt utplacerade nu och ska printa rätt

amount = len(split_list)

for y in range(amount * 10):
    print(numbers_list[y])