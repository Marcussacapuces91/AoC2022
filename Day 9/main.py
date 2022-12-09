import sys

from time import perf_counter_ns
from pprint import pprint

def move(pt: complex, dir: str) -> complex:
    match dir:
        case 'L':
            return pt - 1
        case 'R':
            return pt + 1
        case 'U':
            return pt + complex(0,1)
        case 'D':
            return pt - complex(0,1)
    raise Exception(f"Erreur : dir = {dir}!")


def follow(pt: complex, diff: complex) -> complex:
    match diff.real**2 + diff.imag**2:
        case 0 | 1 | 2:
            return pt
        case 4:
            if diff.real == 0:
                return pt + complex(0, diff.imag / 2)
            else:
                return pt + diff.real / 2
        case 5 | 8:
            return pt + complex(diff.real / abs(diff.real), diff.imag / abs(diff.imag))
    raise Exception(f"Erreur : {diff.real**2 + diff.imag**2}!")


def response1(_lines: list[list]) -> str:
    H = complex(0, 0)
    T = complex(0, 0)
    passe = set()
    for _dir, _len in _lines:
        for _ in range(_len):
            H = move(H, _dir)
            T = follow(T, H-T)
            passe.add(T)

    return f"Réponse 1 : nombre de cases survolées par la queue : {len(passe)}"


def response2(_lines: list[list]) -> str:
    queue = [complex(0,0)] * 10
    passe = set()
    for _dir, _len in _lines:
        for _ in range(_len):
            queue[0] = move(queue[0], _dir)
            for i in range(9):
                diff = queue[i] - queue[i+1]
                while diff.real**2 + diff.imag**2 > 2:
                    queue[i+1] = follow(queue[i+1], queue[i] - queue[i+1])
                    diff = queue[i] - queue[i+1]
            passe.add(queue[9])

    return f"Réponse 2 : nombre de cases survolées par la queue : {len(passe)}"


if __name__ == '__main__':
    with open("input.txt", ) as f:
        full: list[str] = f.read().splitlines()
        f.close()
        lines = []
        for l in full:
            _dir, _len = l.split(' ')
            lines.append((_dir, int(_len)))

        print(f"Longueur du fichier {len(lines)} lignes.")
        s = perf_counter_ns()
        print(response1(lines))
        m = perf_counter_ns()
        print(f"Réponse en {(m - s) / 1000}ms.")
        print(response2(lines))
        e = perf_counter_ns()
        print(f"Réponse en {(e - m) / 1000}ms.")
