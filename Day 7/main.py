import sys

from typing import Generator
from time import perf_counter_ns
from pprint import pprint


def response1(_lines: list[str]) -> str:
    path: str = ""
    size: dict = {}
    for l in _lines:
        match l.split():
            case ['$', 'cd', '/']:
                path = '/'
            case ['$', 'cd', '..']:
                path = path[:path.rfind('/', 0, -1)+1]
            case ['$', 'cd', *dir]:
                path += dir[0] + '/'
            case ['$', 'ls']:
                size[path] = 0
            case ['dir', *dir]:
                pass
            case [*file] if file[0].isnumeric():
                s, n = int(file[0]), file[1]
                for i, d in enumerate(path.split('/')):
                    if i == 0: continue
                    key: str = '/' + '/'.join(path.split('/')[1:i])
                    size[key + ('/' if key[-1] != '/' else '')] += s
            case _:
                print("Erreur : ", l)
        
    sum: int = 0
    for p in size:
        if size[p] < 100000:
            sum += size[p]
    return f"Réponse 1 : Total des répertoires de moins de 100000 : {sum}"


def response2(_lines: str) -> str:
    path: str = ""
    size: dict = {}
    for l in _lines:
        match l.split():
            case ['$', 'cd', '/']:
                path = '/'
            case ['$', 'cd', '..']:
                path = path[:path.rfind('/', 0, -1)+1]
            case ['$', 'cd', *dir]:
                path += dir[0] + '/'
            case ['$', 'ls']:
                size[path] = 0
            case ['dir', *dir]:
                pass
            case [*file] if file[0].isnumeric():
                s, n = int(file[0]), file[1]
                for i, d in enumerate(path.split('/')):
                    if i == 0: continue
                    key: str = '/' + '/'.join(path.split('/')[1:i])
                    size[key + ('/' if key[-1] != '/' else '')] += s
            case _:
                print("Erreur : ", l)
        
    tot: int = 0
    for p in size: tot += size[p]

    need = 30000000 - (70000000 - size['/'])
    for p, s in sorted(size.items(), key=lambda l: l[1], reverse=True):
        if s < need: break
        res = s
    
    return f"Réponse 2 : Taille du plus petit chemin à supprimer : {res}"


if __name__ == '__main__':
    
    
    lines: list[str] = sys.stdin.read().splitlines()
    
    print(f"Longueur du fichier {len(lines)} lignes.")
    s = perf_counter_ns()
    print(response1(lines))
    m = perf_counter_ns()
    print(f"Réponse en {(m - s) / 1000}ms.")
    print(response2(lines))
    e = perf_counter_ns()
    print(f"Réponse en {(e - m) / 1000}ms.")
