from utils import read_data, write_to_file, plot_data
from clarans import Clarans, output_clusters

if __name__ == '__main__':
    # Set parameters
    number_of_medoids = 4
    numlocal = 30
    maxneighbour = 100
    mincost = 999999

    points = read_data()
    clarans_model = Clarans(points, numlocal, maxneighbour, mincost, number_of_medoids)
    medoid_points, medoids = clarans_model.run()
    output_clusters(points, medoids, medoid_points)
    write_to_file('output.txt', points, medoid_points)
    print('ready')
    print(medoids)
    plot_data(points, medoids=medoids)
