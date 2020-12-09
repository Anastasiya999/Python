# 8.1
# SPECYFIKACJA
# Problem: Rozwiązywanie równania liniowego a x + b y + c = 0.
#
# DANE WEJŚCIOWE
# Trzy liczby a, b i c, będące współczynikami równania.
#
# DANE WYJŚCIOWE
# Rozwiązanie równania, w postaci komunikatu
#
# LISTA KROKÓW
# K01: jeżeli a=0 oraz b=0 przejdż do K03, w przeciwnym wypadku do K02
# K02: jeżeli c=0 wypisz "Równanie tożsamościowe.", w przeciwnym wypadku "Równanie sprzeczne. Brak rozwiązań."
# K03: jeżeli a=0 oraz b!=0 wypisz "Rozwiązanie: x = dowolna liczba, y = -c/b" w przeciwnym wypadku przejdż do K04
# K04: jeżeli a!=0 oraz b=0 wypisz "Rozwiązanie: x = -c/a, y = dowolna liczba" w przeciwnym wypadku - "Rozwiązanie: x = dowolna liczba, y = -a/b * x + (-c/b)"


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""

    if a==0 and b==0:
        if c==0:
            print("Równanie tożsamościowe.")
        else:
            print("Równanie sprzeczne. Brak rozwiązań.")
    else:
        if a==0 and b!=0:
            print("Rozwiązanie: x = dowolna liczba, y = {}".format(-c/b))

        elif a!=0 and b==0:
            print("Rozwiązanie: x = {}, y = dowolna liczba".format(-c/a))

        else:
            print("Rozwiązanie: x = dowolna liczba, y = {} * x + ({})".format(-a/b, -c/b))


print("Równanie 5x + 8 = 0")
solve1(5, 0, 8)

print("Równanie 2y + 4 = 0")
solve1(0, 2, 4)

print("Równanie 10x + 5y + 11 = 0")
solve1(10, 5, 11)

print("Równanie 0x + 0y + 4 = 0")
solve1(0, 0, 4)

print("Równanie 0x + 0y + 0 = 0")
solve1(0, 0, 0)