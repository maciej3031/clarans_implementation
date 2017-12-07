import math
import random
import time

import numpy as np
from tqdm import tqdm

random.seed()


class Point(object):
    """
    Klasa reprezentująca punkt jako model danych do klasteryzacji. Posiada 3 atrybuty:
    - współrzędne: x i y
    - przypisany klaster: clusters w formie indeksu obiektu, który jest najbliższym medoidem.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

    def __repr__(self):
        return "Point: X={} Y={}".format(self.x, self.y)


class Polygon(object):
    """
    Klasa reprezentująca poligon jako model danych do klasteryzacji. Posiada 2 atrybuty:
    - listę wierzchołków vertices, gdzie każdy z nich jest instancją klasy Point.
    - przypisany klaster: clusters w formie indeksu obiektu, który jest najbliższym medoidem.
    """
    def __init__(self, vertices):
        self.vertices = vertices
        self.cluster = None

    def __repr__(self):
        return "Polygon: vertices: {}".format(self.vertices)


class Clarans(object):
    """
    Klasa implementująca algorytm CLARANS.
    """

    # Punkt 1 algorytmu.
    # Inicjalizacja parametrów wejściowych.

    def __init__(self, objects, numlocal, maxneighbor, number_of_medoids, polygons=False):
        self.polygons = polygons
        self.objects = objects                # inicjalizacja listy obiektów do klasteryzacji.
        self.objects_indices = len(objects)   # zapisanie do zmiennej indeksów wszystkich obiektów
        self.numlocal = numlocal            # inicjalizacja parametru wejściowego numlocal
        self.maxneighbor = maxneighbor      # inicjalizacja parametru wejściowego maxneighbor
        self.mincost = 10000000000000       # inicjalizacja mincost jako bardzo duża liczba
        self.number_of_medoids = number_of_medoids     # zapisanie do zmiennej liczby szukanych medoidów/klastrów

        self.local_best_medoids = []    # inicjalizacja listy przechowującej lokalne najlepsze rozwiązanie
        self.best_medoids = []          # inicjalizacja listy przechowujacej globalne najlepsze rozwiązanie

        # Inicjalizacja dwuwymiarowej tablicy przechowującej odległości między medoidami a wszystkimmi obiektami, gdzie
        # ij-ty element odpowiada odległości i-tego medoida od j-tego obiektu. Wstępnie wypełniona zerami.
        self.distance_matrix = np.asmatrix(np.zeros((self.number_of_medoids, self.objects_indices)))

    def run(self):
        start_time = time.time()
        pbar = tqdm(total=self.numlocal)

        i = 1  # inicjalizacja i = 1
        while i <= self.numlocal:
            pbar.update(1)
            self.distance_matrix.fill(0)
            self.local_best_medoids = []

            # Punkt 2 algorytmu.
            # Wybranie wstępnych losowych medoidów i zapisanie ich indeksów do listy temp_medoids.
            # Następnie obliczenie odleglości i wypełnienie tablicy distance_matrix przy pomocy metody set_distances()
            # oraz przypisanie obiektom najbliższego medoida, a dokładniej indeksu najbliższego medoida.
            # Na koniec obliczenie początkowego kosztu cost przy pomocy metody get_total_distance()

            temp_medoids = self.get_random_medoids()
            self.set_distances(temp_medoids)
            self.assign_to_clasters(temp_medoids)
            cost = self.get_total_distance(temp_medoids)

            # Punkt 3 algorytmu. Inicjalizacja j = 1.
            j = 1
            while j <= self.maxneighbor:

                # Punkt 4 algorytmu.
                # Wybranie losowego sąsiada przy pomocy metody get_random_neighbor() i zamienienie go z jednym,
                # losowo wybranym obecnym medoidem. Następnie obliczenie odleglości i aktualizacja tablicy
                # distance_matrix przy pomocy metody update_distance_matrix_for_new_medoid() oraz obliczenie kosztu
                # new_cost przy pomocy metody get_total_distance()

                new_medoid_index = self.get_random_neighbor(temp_medoids)
                self.replace_random_medoid(temp_medoids, new_medoid_index)
                self.update_distance_matrix_for_new_medoid(temp_medoids, new_medoid_index)
                self.assign_to_clasters(temp_medoids)
                new_cost = self.get_total_distance(temp_medoids)

                # Punkt 5 algorytmu.
                # Sprawdzenie warunku czy nowy koszt jest mniejszy od aktualnego.
                # Jeżeli tak to pozostaw nowąlistę medoidów jako aktualne najlepsze lokalnie rozwiązanie
                # oraz ustaw aktualny koszt jako koszt nowego węzła. Wróć do punktu 3.

                if new_cost < cost:
                    self.local_best_medoids = temp_medoids.copy()
                    cost = new_cost
                    j = 1
                    continue
                else:

                    # Punkt 6 algorytmu.
                    # Jeżeli nie spełniono punktu 5 to zwiększ j o 1. Jeżeli j jest mniejsze równe od wartości
                    # parametru maxneighbor to wróć do punktu 4

                    j += 1
                    if j <= self.maxneighbor:
                        continue

                    # Punkt 7 algorytmu.
                    # Jeżeli j jest większe od wartości parametru maxneighbor to porównaj wartość aktualnego kosztu
                    # z wartością aktualnego minimalnego kosztu mincost.
                    # Jeżeli jest mniejsza niż mincost to ustaw mincost równe aktualnemu kosztowi oraz ustaw aktualne
                    # najlepsze lokalnie rozwiązanie jako najlepsze rozwiązanie globalne

                    elif cost < self.mincost:
                        self.mincost = cost
                        self.best_medoids = self.local_best_medoids.copy()
                        print("\nNowy minimalny koszt: {} ".format(self.mincost))

                    # Punkt 8 algorytmu.
                    # Zwiększenie i o 1. Jeżeli i > numlocal to zakończ, oblicz odległości,
                    # wypełnij tablicę distance_matrix przy pomocy metody set_distances(), przypisz wszystkim obiektom
                    # indeks najbliższego medoida i zwróć najlepsze globalnie rozwiązanie.
                    # W przeciwnym razie wróć do punktu 2.

                    i += 1
                    if i > self.numlocal:
                        self.set_distances(self.best_medoids)
                        self.assign_to_clasters(self.best_medoids)
                        print("\nCzas wykonania algorytmu: --- {} sekund ---".format(time.time() - start_time))
                        print("\nMinimalny koszt: {} ".format(self.mincost))
                        return self.best_medoids, self.objects
                    else:
                        break
        pbar.close()

    def get_random_medoids(self):
        """
        Zwraca losowe indeksy obiektów, które służą jako wstępne losowe medoidy.
        """
        return random.sample(range(self.objects_indices), self.number_of_medoids)

    def get_distance(self, objA, objB):
        """
        Zwraca odległość między dwoma obiektami .
        """
        if self.polygons:
            return self.get_polygons_distance(objA, objB)
        else:
            return self.get_points_distance(objA, objB)

    def get_polygons_distance(self, objA, objB):
        """
        Zwraca najmniejszą odległość pomiędzy dwoma poligonami.
        """
        distances = []
        for pontA in objA.vertices:
            for pointB in objB.vertices:
                dst = self.get_points_distance(pontA, pointB)
                distances.append(dst)
        return min(distances)

    @staticmethod
    def get_points_distance(objA, objB):
        """
        Zwraca odległość pomiędzy dwoma obiektami.
        """
        return math.sqrt((objA.x - objB.x) ** 2 + (objA.y - objB.y) ** 2)

    def set_distances(self, medoids_indices):
        """
        Wypełnia tablicę distance_matrix obliczonymi odległościami.
        """
        for medoid_index in medoids_indices:
            for obj_index in range(self.objects_indices):
                self.distance_matrix[medoids_indices.index(medoid_index), obj_index] = \
                    self.get_distance(self.objects[medoid_index], self.objects[obj_index])

    def assign_to_clasters(self, medoids_indices):
        """
        Przypisuje obiektom najbliższe medoidy, a dokładniej indeks najbliższego medoida.
        """
        for obj_index, obj in enumerate(self.objects):
            d = 10000000000000
            idx = obj_index
            for medoid_index in medoids_indices:
                distance = self.distance_matrix[medoids_indices.index(medoid_index), obj_index]
                if distance < d:
                    d = distance
                    idx = medoid_index
            obj.cluster = idx

    def get_total_distance(self, medoids_indices):
        """
        Oblicza całkowity koszt tzn. sumę odległości obiektów od ich najbliższych medoidów.
        """
        tot_dist = 0
        for obj_index, obj in enumerate(self.objects):
            tot_dist += self.distance_matrix[medoids_indices.index(obj.cluster), obj_index]
        return tot_dist

    def get_random_neighbor(self, medoids_indices):
        """
        Z listy obiektów losuje indeks nowego modoida.
        """
        new_medoid_index = random.randrange(0, self.objects_indices, 1)
        while new_medoid_index in medoids_indices:
            new_medoid_index = random.randrange(0, self.objects_indices, 1)

        return new_medoid_index

    def replace_random_medoid(self, medoids_indices, new_medoid_index):
        """
        Zamienie losowego medoida na nowo wylosowanego przy pomocy metody get_ranodm_neighbor().
        """
        medoids_indices[random.randrange(0, len(medoids_indices))] = new_medoid_index

    def update_distance_matrix_for_new_medoid(self, medoids_indices, new_medoid_index):
        """
        Aktualizuje wartości w tablicy distance_matrix po wybraniu nowego medoida.
        """
        for obj_index in range(self.objects_indices):
            self.distance_matrix[medoids_indices.index(new_medoid_index), obj_index] = \
                self.get_distance(self.objects[new_medoid_index], self.objects[obj_index])
