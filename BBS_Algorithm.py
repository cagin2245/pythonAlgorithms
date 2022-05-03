from numpy.random import randint
from sympy import isprime


def BBS():
    p_,q_ = input("İki eşit olmayan asal sayı seçiniz").split()
    p , q = int(p_) , int(q_)
    f = isprime(p)
    s = isprime(q)

    if f == True and s == True:
        if(p==q):
            print("\nİki sayı birbirine eşit")
            return
        if(p < 0 or q < 0):
            print("\nNegatif sayı girildi")
            return
        else:
            M = p * q
            s = randint(1,M-1)
            x0 = (s**2) % M
            n = int(input("Kaç rastgele sayı üretilecek: "))
            xn = (x0** ((2*n) % ((p-1)*(q-1)))) % M
            while(n>0):
                xn_ = (x0 ** ((2 * n) % ((p - 1) * (q - 1)))) % M
                print(xn_)
                n=n-1
    else:
        print("\nGerekli şartları sağlamayan girdi")
if __name__ == '__main__':

    BBS()
