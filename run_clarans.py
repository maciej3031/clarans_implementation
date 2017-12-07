import argparse

from model import Clarans
from utils import read_from_file, write_to_file, plot_data, plot_info

if __name__ == '__main__':
    mincost = 999999

    p = argparse.ArgumentParser()
    p.add_argument('-p', '--polygons', help='Use rectangles instead of points.', action='store_true')
    p.add_argument('--number_of_medoids', help='Number of medoids to find. Default = 10', default=10, type=int)
    p.add_argument('--numlocal', help='Number of local minimum to obtain. Default = 20', default=20, type=int)
    p.add_argument('--maxneighbor', help='Maximal number of neighbors in claster. Default = 80', default=80, type=int)
    p.add_argument('--output', help='Output file name. Default = output.txt', default='output.txt')
    p.add_argument('--input', help='Input file name. Default = data.txt', default='data.txt')
    args = p.parse_args()

    objects = read_from_file(args.input, polygons=args.polygons)

    clarans_model = Clarans(objects, args.numlocal, args.maxneighbor, args.number_of_medoids, args.polygons)
    medoids, objects = clarans_model.run()

    write_to_file(args.output, objects, polygons=args.polygons)
    plot_info(medoids, objects)
    plot_data(objects, medoids=medoids, clusters=True, polygons=args.polygons)
