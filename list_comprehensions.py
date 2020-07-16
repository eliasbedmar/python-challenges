#Trying out list comprehensions


old_list=[1,2,3,4,5,6,7]

new_list = []
new_list_2 = []

for i in old_list:
    new_list.append(i)

print(new_list)

new_list_2 = [i**2 for i in old_list]

print(new_list_2)



latitude = [2, 3, 5, 3, 6, 7]
longitude = [54, 67, 32, 67, 45, 33]

coordinates = [(lat,lon) for lat,lon in zip(latitude, longitude)]
print(coordinates)

_list = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]

print(_list)

h_letters = []
for letter in 'human':
    h_letters.append(letter)

print(h_letters)

h_letters = [letter for letter in 'human']
print(h_letters)

matrix = []

for i in range(0,5):
    matrix.append([])

    for j in range(0,5):
        matrix[i].append(j)

print(matrix)


matrix = [[col for col in range(0,5)] for row in range(0,5)]

print(matrix)





























