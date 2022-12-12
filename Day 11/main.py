import sys
import copy
import gc

from time import perf_counter_ns
from pprint import pprint


class Monkey:
    id: int
    items: list
    analyses: int

    def __init__(self, it: iter):
        self.analyses = 0
        
        self.rank = int(next(it).replace(':',' ').split(' ')[1])
        items = next(it).replace(':',',').replace(' ','').split(',')[1:]
        self.items = list(int(x) for x in items)
        self.oper = next(it).split(': ')[1].split('=')[1]
        self.divis = int(next(it).split('by ')[1])
        self.true = int(next(it).lstrip().split(' ')[5])
        self.false = int(next(it).lstrip().split(' ')[5])
        try:
            _ = next(it)
        except StopIteration as e:
            pass


    def analyse1(self):
        self.analyses += len(self.items)
        for item in self.items:
            new: int = int(eval(self.oper, {'old': item}) / 3)
            if new % self.divis == 0:
                yield self.true, new
            else:
                yield self.false, new
        self.items.clear()


    def analyse2(self):
        self.analyses += len(self.items)
        for item in self.items:
            new: int = eval(self.oper, {'old': item}) % (2*3*5*7*11*13*17*19*23)
            if new % self.divis == 0:
                yield self.true, new
            else:
                yield self.false, new
        self.items.clear()            


    def add(self, item):
        self.items.append(item)


def response1(monkeys: list[list]) -> str:
    for i in range(20):
        for m in monkeys:
            for to, item in m.analyse1():
                monkeys[to].add(item)
    maxi = list(monkeys[j].analyses for j in range(len(monkeys)))
    maxi.sort()
            
    return f"Réponse 1 : produit des 2 singes les plus actifs {maxi[-1]*maxi[-2]}"


def response2(monkeys: list[list]) -> str:
    for i in range(10000):
        for m in monkeys:
            for to, item in m.analyse2():
                monkeys[to].add(item)
        if (i+1) % 1000 == 0:
            print(i+1, list(monkeys[j].analyses for j in range(len(monkeys))))

    maxi = list(monkeys[j].analyses for j in range(len(monkeys)))
    print(maxi)
    maxi.sort()
            
    return f"Réponse 2 : produit des 2 singes les plus actifs {maxi[-1]*maxi[-2]}"


if __name__ == '__main__':
    with open("input.txt", ) as f:
        lines: list[str] = f.read().splitlines()
        f.close()
        monkeys = []
        it = iter(lines)
        while True:
            try:
                monkeys.append(Monkey(it))
            except StopIteration as e:
                break
    
        print(f"Longueur du fichier {len(lines)} lignes.")
        s = perf_counter_ns()
        print(response1(copy.deepcopy(monkeys)))
        m = perf_counter_ns()
        print(f"Réponse en {(m - s) / 1000}ms.")
        print(response2(copy.deepcopy(monkeys)))
        e = perf_counter_ns()
        print(f"Réponse en {(e - m) / 1000}ms.")
