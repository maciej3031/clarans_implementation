## INSTRUKCJA URUCHOMIENIA

1. Utwórz wirtualne środowisko pythona w wersji 3.5.2+ i uruchom je (np.: ```virtualenv venv --python=3.5``` a następnie
 ```venv\Scripts\activate``` dla środowiska Windows lub ```source venv/bin/activate``` dla środowiska linux)
2. Zainstaluj wymagania z pliku ```requirements.txt``` (```pip install -r requirements.txt```).
3. Użyj ```python generate_data.py``` aby wygenerować przykładowe dane. Opcjonalnie użyj ```python show_data.py``` aby zwizualizować dane. Użyj flagi ```-p``` aby wygenerować poligony zamiast punktów.
4. Użyj ```python run_clarans.py``` aby uruchomić algorytm. Wynik zostanie zapisany do katalogu data jako output.txt oraz wyświetlony na ekranie w postaci graficznej. Użyj flagi ```-p``` aby klasteryzować zbiór poligonów.

## IMPLEMENTACJA ALGORYTMU CLARANS (Clustering Large Applications based on Randomized Search)

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

Jako model danych przyjęto punkty w przestrzeni dwuwymiarowej o współrzędnych x i y zaimplementowane jako klasa
o atrybutach x oraz y. Drugim użytym modelem danych przestrzennych są poligony zdefiniowane także w
przestrzeni dwuwymiarowej i zaimplementowane jako klasa z atrybutem vertices będącym listą zawierającą obiekty klasy Punkt.

<br />

 
![alt text](https://github.com/maciej3031/clarans_implementation/blob/master/data/clarans.png)
źródło: Raymond T. Ng, Jiawei Han - "Efficient and Effective Clustering Methods for Spatial Data Mining"

## WYNIKI DLA PRZYKŁADOWYCH DANYCH

 ### Losowo wygenerowane punkty w przestrzeni 2-wymiarowej:

![alt text](https://github.com/maciej3031/clarans_implementation/blob/master/data/sample_data.png)

 ### Wynik działania klasteryzacji algorytmem CLARANS:

![alt text](https://github.com/maciej3031/clarans_implementation/blob/master/data/sample_output.png)