#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:30:52 2019

@author: elias.bedmar.fresneda@ibm.com
"""

#Version used: Python 3.7.0

import csv
import math


centroids = {
    "a": [-0.357, -0.253],      #adam
    "b": [-0.357, -0.253],      #bob
    "c": [2.674, -0.001],       #charley
    "d": [1.033, -1.251],       #david
    "e": [-1.495, -0.090]       #edward
}

print(centroids)


#indexing: 0 - X, 1 - Y, 2 - Centroid, 3 - Error



# def parse_input(input_file_path):
#     with open(input_file_path) as f:
#         reader = csv.reader(f)
#         data_points = []
#         for row in reader:
#             data_points.append(row)
#
#         return data_points





#Algorithm:
#Iterative 2-step K-means run until convergence.

#Step 1: Expectation Step:
#input data point assigned to closest cluster centroid measured using Euclidian distance + Error worked out
# dist = SQRT([x-Cx]2 + [y-Cy]2 )
# Error = SUM of dist for n points

# Step 2: Maximisation Step:
#Total Error metric -> minimised: adjusting cluster centroids to centre of ALL data points assigned to it.
# New centroid of cluster should be found by computing the mean of the point coordinates in each dimension (x, y treated independently)

#Iterate until convergence: Convergence is achieved when expectation step does not change assignment of any data points
# (OR) when Error doesn't change from previous iteration


#Output:
#Plain text file, “OUTPUT.TXT”.
# 1st line: “error = ” followed by the error metric printed to 3 decimal places (i.e. the printf format would be “error = %.3f”)
# Each newline - Cluster name for input points -> for each item in inputs



# class !!!
