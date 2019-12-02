
mass_data = open("C:/Users/sabel/Documents/Python/Advent Code/data_fuel_counter.txt")

operation = 0

for i in mass_data:

    operation += (int(i)//3)-2


print('The sum of the fuel requirement is', operation)
