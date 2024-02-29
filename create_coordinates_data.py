import random

#specify filename to be created to store data
filename = 'coordinates.txt'

# Generate x and y coordinate values
x_values = list(range(1, 101))
y_values = sorted(random.sample(range(1, 1001), 100))
coordinates = list(zip(x_values, y_values))

# Write coordinates to the text file
with open(filename, 'w') as file:
    for x, y in coordinates:
        file.write(f'{x}, {y}\n')

print(f'Coordinates have been written to {filename}')
