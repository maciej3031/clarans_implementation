## INSTRUKCJA URUCHOMIENIA

1. Utwórz wirtualne środowisko pythona w wersji 3.5.2+ i uruchom je (np.: ```virtualenv venv --python=3.5``` a następnie
 ```venv\Scripts\activate``` dla środowiska Windows lub ```source venv/bin/activate``` dla środowiska linux)
2. Zainstaluj wymagania z pliku ```requirements.txt``` (```pip install -r requirements.txt```).

## Opis interfejsu użytkownika
W programie mamy do użytku trzy polecenia:

1. ```python generate_data.py``` – Generuje przykładowe dane do analizy.
Opcjonalne parametry:
- ```-p, --polygons``` – Użyj poligonów zamiast punktów.
- ```--filename nazwa_pliku.txt``` – Nazwa pliku wynikowego z zapisanymi danymi, domyślnie: data.txt.
- ```--clusters_number 10``` – Liczba klastrów w danych, domyślnie: 10.
- ```--objects_number 1000``` – Liczba obiektów (punktów/poligonów) do wygenerowania, domyślnie 1000.

2. ```python show_data.py``` – Wyświetla plik z danymi.
Opcjonalne parametry:
- ```-p, --polygons``` – Użyj poligonów zamiast punktów.
- ```--filename nazwa_pliku.txt``` – Nazwa pliku do wczytania z zapisanymi danymi, domyślnie: data.txt.

3. ```python run_clarans.py``` – Uruchamia algorytm klasteryzacji.
Opcjonalne parametry:
- ```-p, --polygons``` – Użyj poligonów zamiast punktów.
- ```--input nazwa_pliku.txt``` – Nazwa pliku z zapisanymi danymi do wczytania do klasteryzacji, domyślnie: data.txt.
- ```--output nazwa_pliku.txt``` – Nazwa pliku do zapisania wyniku działania algorytmu, domyślnie: output.txt.
- ```--number_of_medoids 10``` – Liczba klastrów/medoidów do poszukiwania, domyślnie 10.
- ```--numlocal 20``` – Wartość parametru numlocal, domyślnie 20.
- ```--maxneighbor 80``` – Wartość parametru maxneighbor domyślnie 80


## IMPLEMENTACJA ALGORYTMU CLARANS (Clustering Large Applications based on Randomized Search)

Algorytm polega na znalezieniu najbardziej reprezentatywnych obiektów w każdym z klastrów dla których to obiektów koszt
(np. suma odległość od pozostałych z nich należących do tego samego klastra) jest minimalny. Obiekty takie nazywamy medoidami.
Po wyborze medoidów każdy z klasterowanych obiektów trafia do klastra, którego reprezentantem jest najbliższy temu obiektowi medoid.
CLARANS opiera się na losowym wyszukiwaniu kandydatów na medoidów, policzeniu kosztu i porównaniu z aktualnym najlepszym lokalnie rozwiązaniem.
Czynność ta jest powtarzana dopóki liczba wybranych pod rząd losowo obiektów, których koszt jest większy od aktualnego
najmniejszego kosztu lokalnego nie przekroczy wartości *maxneighbor*. Wówczas koszt najlepszego rozwiązania lokalnego
jest porównywany z najlepszym do tej pory osiągniętym rozwiązaniem globalnym i jeżeli jest on mniejszy to lokalne
rozwiązanie staje się globalnym. Bez względu na to czy rozwiązanie lokalne stało się globalnym czy nie, licznik
pętli zwiększany jest o 1, a algorytm wykonywany jest od nowa dopóki liczba takich przejść pętli nie osiągnie
wartości *numlocal*. Wówczas zwracane jest aktualnie najlepsze globalnie rozwiązanie.

1. Parametry wejściowe *numlocal* i *maxneighbor*. Zainicjalizuj *i = 1* oraz *mincost* równy bardzo dużej liczbie.
2. Wybierz losowe obiekty i ustaw je jako aktualne rozwiązanie, oblicz dla nich koszt.
3. Zainicjalizuj *j = 1*.
4. Wybierz losowego sąsiada i utwórz rozwiązanie *S* a następnie oblicz dla niego koszt.
5. Jeżeli wartość kosztu dla *S* jest mniejsza to ustaw aktualne lokalne rozwiązanie jako *S* i wróć do punktu 3.
6. W przeciwnym razie zwiększ *j* o *1*. Jeżeli *j <= maxneighbor* wróć do punktu 4.
7. W przeciwnym razie jeżeli *j* > *maxneighbor* porównaj koszt dla aktualnego lokalnego rozwiązania z wartością kosztu
   *mincost* dla najlepszego globalnego rozwiązania. Jeżeli jest mniejszy niż *mincost* to ustaw *mincost* równe kosztowi
   aktualnego lokalnego rozwiązania oraz ustaw aktualne lokalne rozwiązanie jako najlepsze globalne. 
8. Zwiększ *i* o *1*. Jeżeli *i > numlocal* to zakończ i zwróć najlepsze globalnie rozwiązanie. W przeciwnym razie wróć do punktu 2. 
 
 <br />
 <br />
 
## MODEL DANYCH PRZESTRZENNYCH

Jako model danych przyjęto punkty w przestrzeni dwuwymiarowej o współrzędnych x i y zaimplementowane jako klasa o atrybutach x oraz y.
Drugim modelem danych przestrzennych użytych do analizy są poligony zdefiniowane także w przestrzeni dwuwymiarowej, zaimplementowane
jako klasa z atrybutem vertices będącym listą zawierającą obiekty klasy Punkt należące do poligonu.
Koszt został zaimplementowany:
- dla punktów jako suma odległości pomiędzy wszystkimi punktami w poszczególnych klastrach a medoidami w tych klastrach.
- dla poligonów jako suma najmniejszej odległości pomiędzy wierzchołkami wszystkich poligonów w poszczególnych klastrach a poligonami będącymi medoidami w tych klastrach.


<br />

 
![alt text](https://github.com/maciej3031/clarans_implementation/blob/master/data/clarans.png)
źródło: Raymond T. Ng, Jiawei Han - "Efficient and Effective Clustering Methods for Spatial Data Mining"

## WYNIKI DLA PRZYKŁADOWYCH DANYCH

 ### Losowo wygenerowane punkty w przestrzeni 2-wymiarowej:

![alt text](https://github.com/maciej3031/clarans_implementation/blob/master/data/sample_data.png)

 ### Wynik działania klasteryzacji algorytmem CLARANS:

![alt text](https://github.com/maciej3031/clarans_implementation/blob/master/data/sample_output.png)

 ### Losowo wygenerowane poligony w przestrzeni 2-wymiarowej:

![alt text](https://github.com/maciej3031/clarans_implementation/blob/master/data/sample_polygons_data.png)

 ### Wynik działania klasteryzacji algorytmem CLARANS:

![alt text](https://github.com/maciej3031/clarans_implementation/blob/master/data/sample_polygons_output.png)