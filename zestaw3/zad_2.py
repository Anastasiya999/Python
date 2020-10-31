#L = [3, 5, 4] ; L = L.sort()   metoda sort zwraca None, dla tego tutaj przypisanie nie jest poprawne jeżeli chcemy dalej operowac na L
#prawidłowy zapis:
L=[3,5,4]; L.sort()           #metoda sort dokonuje sortowania na referencji, a nie kopii listy
                              #jeżeli nie chcemy dokonywać zmian w L, a stworzyć nową posortowana listę na podstawi L, 
                              # należy skorzystac z metody sorted(L), która zwraca nową listę
#----------------------------------------------------------------------------------------------------------

#x, y = 1, 2, 3               nieprawidłowa składnia, dla przypisania zbiorczego oczekiwane dwie wartosci a nie trzy
#prawidłowy zapis:
x, y= 1, 2 
#lub
x, y, z=1, 2, 3
#----------------------------------------------------------------------------------------------------------

#X = 1, 2, 3 ; X[1] = 4  #X-krotka, więc jej zawartość niezmienna, przypisanie X[1]=4 będzie powodować typeError
#----------------------------------------------------------------------------------------------------------

#X = [1, 2, 3] ; X[3] = 4  X lista trójelementowa, przypisania X[3]=4 jest nieprawidłowe skladniowo, ponieważ indeks 3 jest poza listą
                           #jeżeli chodzi o dodaniu elementu na koniec listy należy użyć metody append: X.append(3)
#----------------------------------------------------------------------------------------------------------

#X = "abc" ; X.append("d")  X jest typu str, więc nie można wywołać metody append na X
                           #jeżeli chcemy dodać nowy element, to używamy X=X+"d"
#----------------------------------------------------------------------------------------------------------

#L = list(map(pow, range(8)))  metoda pow() przyjmuje dwa argumenty a nie jeden,więc należy jeszcze dodać drugą zmienną typu iterable, która okresła potęge liczb
#----------------------------------------------------------------------------------------------------------

                           