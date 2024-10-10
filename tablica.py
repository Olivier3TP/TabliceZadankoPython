import random


class Tablica:
    def __init__(self, n):
        self.tablica = [0] * n

    def wypelnij(self, min_zakres, max_zakres):
        for i in range(self.tablica):
            self.tablica.append(random.randint(min_zakres, max_zakres))

    def wyswietl(self):
        print(self.tablica)