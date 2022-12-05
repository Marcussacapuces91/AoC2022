from typing import Generator
from time import perf_counter_ns


def decoupe(_lines: list) -> Generator:
    lines = iter(_lines)
    while True:
        line = next(lines)
        if line == "":
            break

    for line in lines:
        _, nb, _, src, _, dst = line.split()
        yield int(nb), int(src)-1, int(dst)-1
        

def initState(_lines: list):
    yield list("QWPSZRHD")
    yield list('VBRWQHF')
    yield list('CVSH')
    yield list('HFG')
    yield list('PGJBZ')
    yield list('QTJHWFL')
    yield list('ZTWDLVJN')
    yield list('DTZCJGHF')
    yield list('WPVMBH')


def response1(_state, _lines: Generator) -> str:
    states = list(_state)
    for nb, src, dst in _lines:
        for i in range(nb):
            states[dst] += states[src].pop()
    return f"Réponse 1 : {''.join(i[-1] for i in states)}"


def response2(_state, _lines: Generator) -> str:
    states = list(_state)
    for nb, src, dst in _lines:
        states[dst] += states[src][-nb:]
        del states[src][-nb:]
    return f"Réponse 2 : {''.join(i[-1] for i in states)}"


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines: list[str] = f.read().splitlines()

        print(f"Longueur du fichier {len(lines)} lignes.")
        s = perf_counter_ns()
        print(response1(initState(lines), decoupe(lines)))
        m = perf_counter_ns()
        print(f"Réponse en {(m - s) / 1000}ms.")
        print(response2(initState(lines), decoupe(lines)))
        e = perf_counter_ns()
        print(f"Réponse en {(e - m) / 1000}ms.")
        f.close()
