#Author : Jasmin Velagic-Ramadani
#Date : 2024-09-18

print('Ei23 - genrep praktiskt prov ht24')
resistor_varde = (input('Vad är ditt resistor värde?'))

resistor_varde = resistor_varde.split(' ')

serieresistans = 0
pararellresistans = 0

antal_resistorer = len(resistor_varde)

for i in range(0, antal_resistorer):
    serieresistans += int(resistor_varde[i])
    pararellresistans += (1 / int(resistor_varde[i]))
pararellresistans = 1 / pararellresistans

print(f'Serieresistans :{serieresistans}')
print(f'Pararellresistans: {pararellresistans}')
