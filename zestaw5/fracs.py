__all__=['sub_frac','add_frac','mul_frac','div_frac','cmp_frac','is_positive','is_zero','frac2float']
import math

def add_frac(frac1, frac2):         # frac1 + frac2
 
    licznik=frac1[0]*frac2[1]+frac2[0]*frac1[1]
    mianownik=frac1[1]*frac2[1]

    a=math.gcd(licznik,mianownik)
    licznik, mianownik=licznik/a, mianownik/a
    result=list([licznik,mianownik])

    check_zeroDiv(result)
    check_denom(result)

    if is_zero(result):
        return 0
    else:
        return result   

def sub_frac(frac1, frac2):      # frac1 - frac2

    licznik=frac1[0]*frac2[1]-frac2[0]*frac1[1]
    mianownik=frac1[1]*frac2[1]

    a=math.gcd(licznik,mianownik)
    licznik, mianownik=licznik/a, mianownik/a
    result=list([licznik,mianownik])

    check_zeroDiv(result)
    check_denom(result)

    if is_zero(result):
        return 0
    else:
        return result 
def mul_frac(frac1, frac2):         # frac1 * frac2

    licznik=frac1[0]*frac2[0]
    mianownik=frac1[1]*frac2[1]

    a=math.gcd(licznik,mianownik)
    licznik, mianownik=licznik/a, mianownik/a
    result=list([licznik,mianownik])

    check_zeroDiv(result)
    check_denom(result)
    if is_zero(result):
        return 0
    else:
        return result   
def div_frac(frac1, frac2):         # frac1 / frac2
    check_zeroDiv(frac1)
    check_zeroDiv(frac2)

    licznik=frac1[0]*frac2[1]
    mianownik=frac1[1]*frac2[0]

    a=math.gcd(licznik,mianownik)
    licznik, mianownik=licznik/a, mianownik/a
    result=list([licznik,mianownik])

    
    check_denom(result)
    if is_zero(result):
        return 0
    else:
        return result   

def is_positive(frac):             # bool, czy dodatni
    check_denom(frac)
    if frac[0]<0:
        return False
    else:
        return True



def is_zero(frac):                # bool, typu [0, x]
    if frac[0]==0 and frac[1]!=0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    check_zeroDiv(frac1)
    check_zeroDiv(frac2)
    check_denom(frac1)
    check_denom(frac2)
    
    
    frac1[0]=frac1[0]*frac2[1]
    frac2[0]=frac2[0]*frac1[1]
    
    if frac1[0]<frac2[0]:
        return -1
    elif frac1[0]>frac2[0]:
        return 1
    else:
        return 0

   
def frac2float(frac):             # konwersja do float
    check_zeroDiv(frac)
    return float(frac[0]/frac[1])

def check_denom(frac):
    if frac[1]<0:
        frac[0]*=-1
        frac[1]*=-1

def check_zeroDiv(frac):
    if frac[1]==0:
        raise ZeroDivisionError

