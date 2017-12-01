import argparse
import os
import random

from utils import plot_data, read_from_file

random.seed()


def generate_data(filename, clusters_number):
    with open(os.path.join('data', filename), 'w+') as f:
        for m in range(5, clusters_number + 5):
            xx = random.randrange(0, 300, 1) + random.randrange(100, 300, 1) * m
            yy = random.randrange(0, 300, 1) + random.randrange(100, 300, 1) * m
            n = random.randrange(50, 100, 1)
            for i in range(n):
                r_plus_x = random.randrange(1, 30, 1)
                r_minus_x = random.randrange(1, 300, 1)
                r_plus_y = random.randrange(1, 300, 1)
                r_minus_y = random.randrange(1, 300, 1)
                x = random.randrange(xx - r_minus_x, xx + r_plus_x, 1)
                y = random.randrange(yy - r_minus_y, yy + r_plus_y, 1)
                point = "{} {}\n".format(x, y)
                f.write(point)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--filename', help='Output file name. Default = data.txt.', default='data.txt')
    p.add_argument('--clusters_number', help='Number of clusters. Default = 8.', default=8, type=int)
    args = p.parse_args()

    generate_data(args.filename, args.clusters_number)
    print('Data saved to file {}'.format(args.filename))

    points = read_from_file(args.filename)
    plot_data(points)
