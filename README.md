## INSTRUKCJA URUCHOMIENIA

1. Utwórz wirtualne środowisko pythona w wersji 3.5.2+ i uruchom je.
2. Zainstaluj wymagania z pliku ```requirements.txt``` (```pip install -r requirements.txt```).
3. Użyj ```python generate_data.py``` aby wygenerować przykładowe dane. Opcjonalnie użyj ```python show_data.py``` aby zwizualizować dane.
4. Użyj ```python run_clarans.py``` aby uruchomić algorytm.

## IMPLEMENTACJA ALGORYTMU CLARANS

1. Parametry wejściowe *numlocal* i *maxneighbor*. Zainicjalizuj *i = 1* oraz *mincost* równy bardzo dużej liczbie.
2. Wybierz węzeł grafu i ustaw go jako aktualny.
3. Zainicjalizuj *j = 1*.
4. Wybierz losowego sąsiada *S* węzła aktualnego a następnie oblicz funkcję kosztu dla nich obu.
5. Jeżeli wartość funkcji kosztu dla *S* jest mniejsza to ustaw aktualny węzeł jako *S* i wróć do punktu 3.
6. W przeciwnym razie zwiększ *j* o *1*. Jeżeli *j <= maxneighbor* wróć do punktu 4.
7. W przeciwnym razie jeżeli *j > maxneighbor* porównaj funkcję kosztu dla węzła aktualnego z wartością aktualnego minimalnego kosztu *mincost*.
 Jeżeli jest mniejsza niż *mincost* to ustaw *mincost* równe aktualnemu kosztowi oraz ustaw aktualny węzeł jako najlepszy węzeł *bestnode*.
8. Zwiększ *i* o *1*. jeżeli *i > numlocal* to zakończ i zwróć *bestnode*. W przeciwnym razie wróć do punktu 2.
 
 <br />
 <br />
 
![alt text](https://github.com/maciej3031/clarans_implementation/blob/master/clarans.png)
źródło: Raymond T. Ng, Jiawei Han - "Efficient and Effective Clustering Methods for Spatial Data Mining"

## WYNIKI DLA PRZYKŁADOWYCH DANYCH

 ### Losowo wygenerowane punkty w przestrzeni 2-wymiarowej:

![alt text](https://github.com/maciej3031/clarans_implementation/blob/master/data/sample_data.png)

 ### Wynik działania algorytmu CLARANS:

![alt text](https://github.com/maciej3031/clarans_implementation/blob/master/data/sample_output.png)