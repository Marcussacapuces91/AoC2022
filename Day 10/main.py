import sys

from time import perf_counter_ns
from pprint import pprint


def get_registers(_lines: list[list]) -> list[int]:
    reg: list = [1]
    for line in _lines:
        match line:
            case ('addx', val):
                reg.append(reg[-1])
                reg.append(reg[-1] + val)
            case 'noop':
                reg.append(reg[-1])
            case _:
                raise Exception(f"Erreur : {line}!")
    return reg

def response1(_lines: list[list]) -> str:
    reg = get_registers(_lines)
    sum: int = 0
    for i, c in enumerate(reg):
        if i+1 in [20,60,100,140,180,220]:
            sum += (i+1) * c
    
    return f"Réponse 1 : fréquence : {sum}"


def response2(_lines: list[list]) -> str:
    reg = get_registers(_lines)
    res: str = f"Réponse 2 : afficheur\n"
    for i, c in enumerate(reg):
        if i % 40 == 0: res += "\n"
        res += '#' if i % 40 in [c-1,c,c+1] else ' '
    return res


if __name__ == '__main__':
    with open("input.txt", ) as f:
        full: list[str] = f.read().splitlines()
        f.close()
        lines = []
        for l in full:
            try:
                _cmd, _val = l.split(' ')
                lines.append( (_cmd, int(_val)) )
            except ValueError as E:
                lines.append( l )

        print(f"Longueur du fichier {len(lines)} lignes.")
        s = perf_counter_ns()
        print(response1(lines))
        m = perf_counter_ns()
        print(f"Réponse en {(m - s) / 1000}ms.")
        print(response2(lines))
        e = perf_counter_ns()
        print(f"Réponse en {(e - m) / 1000}ms.")
