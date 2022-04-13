# kilometers_value = miles_value * 1.609344
miles = input('Enter a distance in miles: ')
# we receive the varaible(miles) as string

# transfere the miles into float type
miles_flo = float(miles)
milesInKm = miles_flo * 1.609344

print("Equals km")
print(milesInKm)