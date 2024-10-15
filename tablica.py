import random


class Tablica:
    def __init__(self, n):
        self.rozmiar = n
        self.tablica = [0] * n
    def wypelnij(self, min_zakres, max_zakres):
        for i in range(self.rozmiar):
            self.tablica[i] = random.randint(min_zakres, max_zakres)
    def wyswietl(self):
        print(self.tablica)
    def maximum(self):
        wartosc_max = self.tablica[0]
        for liczba in self.tablica:
            if liczba > wartosc_max:
                wartosc_max = liczba
        return wartosc_max
    def maximum_2(self):
        self.tablica.sort()
        return self.tablica[-2]
    def minimum(self):
        wartosc_min = self.tablica[0]
        for liczba in self.tablica:
            if liczba < wartosc_min:
                wartosc_min = liczba
        return wartosc_min
    def znajdz_wartosc(self, wartosc=0):
        for i in range(self.rozmiar):
            if self.tablica[i] == wartosc:
                return i
