import math
import random

import numpy as np

random.seed()

"""
1. Input parameters numlocal and maxneighbor. Initialize i to 1, and mincost to a large number.
2. Set current to an arbitrary node in G_{n,k}
3. Set j to 1.
4. Consider a random neighbor S of current, and based on Equation (5) calculate the cost differential 
    of the two nodes.
5. If S has a lower cost, set current to S, and go to Step (3).
6. Otherwise, increment j by 1. If j<=maxneighbor,go to Step (4).
7. Otherwise, when j > maxneighbor, compare the cost of current with mincost. If the former is less than mincost, 
    set mincost to the cost of current, and set bestnode to current.
8. Increment i by 1. If i > numlocal, output bestnode and halt. Otherwise, go to Step (2).
"""


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Clarans(object):
    def __init__(self, points, numlocal, maxneighbor, mincost, number_of_medoids):
        self.points = points
        self.numlocal = numlocal
        self.maxneighbor = maxneighbor
        self.mincost = mincost
        self.number_of_medoids = number_of_medoids
        self.local_best_node = []
        self.best_node = []

    def run(self):
        i = 1
        N = len(self.points)
        d_mat = np.asmatrix(np.zeros((self.number_of_medoids, N)))

        while i <= self.numlocal:
            # Step 2 - pick k random medoids from data points - medoids_nr from points
            node = np.random.permutation(range(N))[:self.number_of_medoids]
            fill_distances(d_mat, self.points, node)
            cls = assign_to_closest(self.points, node, d_mat)
            cost = total_dist(d_mat, cls)
            copy_node = node.copy()
            print('new start \n')
            # increase neighbor count
            j = 1

            while j <= self.maxneighbor:
                # Step 4 - pick a random neighbor of current node - i.e change randomly one medoid
                # calculate the cost differential of the initial node and the random neighbor
                idx = pick_and_replace_random_neighbor(copy_node, N)
                update_distances(d_mat, self.points, copy_node, idx)
                cls = assign_to_closest(self.points, copy_node, d_mat)
                new_cost = total_dist(d_mat, cls)

                # check if new cost is smaller
                if new_cost < cost:
                    cost = new_cost
                    self.local_best_node = copy_node.copy()
                    print('Best cost: ' + str(cost) + ' ')
                    print(self.local_best_node)
                    print('\n')
                    j = 1
                    continue
                else:
                    j = j + 1
                    if j <= self.maxneighbor:
                        continue
                    else:
                        if self.mincost > cost:
                            self.mincost = cost
                            print("change bestnode ")
                            print(self.best_node)
                            print(" into")
                            self.best_node = self.local_best_node.copy()
                            print(self.best_node)
                            print('\n')

                i = i + 1
                if i > self.numlocal:
                    fill_distances(d_mat, self.points, self.best_node)
                    cls = assign_to_closest(self.points, self.best_node, d_mat)
                    print("Final cost: " + str(self.mincost) + ' ')
                    print(self.best_node)
                    print('\n')
                    return cls, self.best_node
                else:
                    break


def pick_and_replace_random_neighbor(current_node, set_size):
    # pick a random item from the set and check that it is not selected
    node = random.randrange(0, set_size, 1)
    while node in current_node:
        node = random.randrange(0, set_size, 1)

    # replace a random node
    i = random.randrange(0, len(current_node))
    current_node[i] = node
    return i


def dist_euc(pointA, pointB):
    return math.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2)


def assign_to_closest(points, meds, d_mat):
    cluster = []
    for i in range(len(points)):
        if i in meds:
            cluster.append(np.where(meds == i))
            continue
        d = 999999
        idx = i
        for j in range(len(meds)):
            d_tmp = d_mat[j, i]
            if d_tmp < d:
                d = d_tmp
                idx = j
        cluster.append(idx)
    return cluster


def fill_distances(d_mat, points, current_node):
    for i in range(len(points)):
        for k in range(len(current_node)):
            d_mat[k, i] = dist_euc(points[current_node[k]], points[i])


def total_dist(d_mat, cls):
    tot_dist = 0
    for i in range(len(cls)):
        tot_dist += d_mat[cls[i], i]
    return tot_dist


def update_distances(d_mat, points, node, idx):
    for j in range(len(points)):
        d_mat[idx, j] = dist_euc(points[node[idx]], points[j])


def output_clusters(points, medoids, medoid_points):
    for i in range(len(points)):
        medoid_points[i] = medoids[medoid_points[i]]
