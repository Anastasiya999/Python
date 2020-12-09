# 8.3
import random

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    circle_points = 0
    square_points = 0
    random.getstate()

    for i in range(n):
        
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            circle_points += 1

        square_points += 1
        pi = 4 * circle_points / square_points

    return pi




print(calc_pi(1000))
# nawet zwiększając liczbę iteracji do 1000 za każdym razem będziemy otrzymywać inną dokładność Pi, nie zawsze lepszą. Ponieważ generowane liczby trafiają w obszar 
# okręga za każdym razem w sposób losowy, czasem to daje większą dokładność przy odnośnie małej liczbie iteracji(100), a czasem mniejszą.

