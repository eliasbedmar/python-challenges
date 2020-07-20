
#!/usr/bin/env python

import csv
import math as m
import pandas as pd



def parse_input(file_path):
    with open(file_path) as f:
        csv_reader = csv.reader(f)

        clean_results = []
        for row in csv_reader:
            clean_results.append(row)

    n = len(clean_results)

    return clean_results, n

clean_results, n = parse_input('input.csv')

print(clean_results)



data_object = {}

for (i, points) in zip(range(n),clean_results):
    coord_x, coord_y = float(points[0]), float(points[1])
    data_object.update({i: [coord_x,coord_y]})

print(data_object)




####Processing

#Calculate distance wrt all centroids

def distance(x, y, centroids):
    #A
    Cx, Cy = centroids['A'][0],centroids['A'][1]
    dist_a = m.sqrt((x - Cx) ** 2 + (y - Cy) ** 2)
    #B
    Cx, Cy = centroids['B'][0], centroids['B'][1]
    dist_b = m.sqrt((x - Cx) ** 2 + (y - Cy) ** 2)
    #C
    Cx, Cy = centroids['C'][0], centroids['C'][1]
    dist_c = m.sqrt((x - Cx) ** 2 + (y - Cy) ** 2)
    #D
    Cx, Cy = centroids['D'][0], centroids['D'][1]
    dist_d = m.sqrt((x - Cx) ** 2 + (y - Cy) ** 2)
    #E
    Cx, Cy = centroids['E'][0], centroids['E'][1]
    dist_e = m.sqrt((x - Cx) ** 2 + (y - Cy) ** 2)

    result_list = [dist_a,dist_b,dist_c,dist_d,dist_e]
    min_dist = min(result_list)
    if dist_a == min_dist:
        centroid = 'Centroid A'
        return dist_a, centroids['A'][0], centroids['A'][1], 'A'
    elif dist_b == min_dist:
        centroid = 'Centroid B'
        return dist_b, centroids['B'][0], centroids['B'][1], 'B'
    elif dist_c == min_dist:
        centroid = 'Centroid C'
        return dist_c, centroids['C'][0], centroids['C'][1], 'C'
    elif dist_d == min_dist:
        centroid = 'Centroid D'
        return dist_d, centroids['D'][0], centroids['D'][1], 'D'
    else:
        centroid = 'Centroid E'
        return dist_e, centroids['E'][0], centroids['E'][1], 'E'


#Iteration 0

centroids = {
    "A": [-0.357, -0.253],
    "B": [-0.055, 4.392],
    "C": [2.674, -0.001],
    "D": [1.044, -1.251],
    "E": [-1.495, -0.090]
}

def processing(data_object):
    for coord in data_object:
        x = data_object[coord][0]
        y = data_object[coord][1]
        dist, Cx, Cy, cluster = distance(x, y, centroids)
        data_object[coord].append(dist)
        data_object[coord].append(Cx)
        data_object[coord].append(Cy)
        data_object[coord].append(cluster)
    print(data_object)

processing(data_object)


#Data object:
#key: [0.CoordX,1.CoordY,2.ERR,3.CentrX,4.Centr,5.Cluster]


#Calculate total error
total_error = float(0)
for point in data_object:
    total_error += data_object[point][2]

print(total_error)

#Recalculate Cluster centroids

df=pd.DataFrame.from_dict(data_object, orient='index', columns=['0.CoordX','1.CoordY','2.ERR','3.CentrX','4.Centr','5.Cluster'])
print(df)

filter = df.groupby(['5.Cluster']).mean()
print(filter)

centroids = {}
for key in ['A','B','C','D','E']:
    centroids[key] = [filter['0.CoordX'][key], filter['1.CoordY'][key]]

print('ITERATION 0')
print('Centroids: ')

print(centroids)

print('Total Error: ')

print(total_error)


######<----------------------------------------------------->####




#Output:
#Output.txt -  plain text file that contains the following output,
# the first line will have “error = ” followed by the error metric printed to 3 decimal places (i.e. the printf format would be “error = %.3f”).
# Each of the following lines will be the cluster name for the input points in the same order as it appeared in the input data file.
# Also print new Centroids