import argparse

from model import Clarans
from utils import read_from_file, write_to_file, plot_data

if __name__ == '__main__':
    # Set parameters
    mincost = 999999

    p = argparse.ArgumentParser()
    p.add_argument('--number_of_medoids', help='Number of medoids to find.', default=5, type=int)
    p.add_argument('--numlocal', help='Number of local minimum to obtain.', default=15, type=int)
    p.add_argument('--maxneighbour', help='Maximal number of neighbours in claster.', default=100, type=int)
    p.add_argument('--output', help='Output file name.', default='output.txt')
    p.add_argument('--input', help='Input file name.', default='data.txt')
    args = p.parse_args()

    points = read_from_file(args.input)

    clarans_model = Clarans(points, args.numlocal, args.maxneighbour, args.number_of_medoids)
    medoids, points = clarans_model.run()

    write_to_file(args.output, points)

    print('\nSuccess!')
    print("Medoids found:")
    for i in medoids:
        print("Point {}, co-ordinates: X={}, Y={}".format(i, points[i].x, points[i].y))
    plot_data(points, medoids=medoids, clusters=True)
