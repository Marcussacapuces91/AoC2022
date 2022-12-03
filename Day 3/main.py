from typing import Generator
from time import perf_counter_ns


def decoupe(_lines: list) -> Generator:
    for line in _lines:
        l2: int = int(len(line)/2)
        yield line[:l2], line[-l2:]


def response1(_lines: Generator) -> str:
    sum: int = 0
    for l, r in _lines:
        for c in l:
            if c in r:
                if c.islower():
                    sum += ord(c)-96
                else:
                    sum += ord(c)-65+27
                break
            
    return f"Resultat 1 : {sum}"


def response2(_lines: Generator) -> str:
    return f"Resultat 2."


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines: list[str] = f.read().splitlines()

        print(f"Nombre de sacs {len(lines)}")
        s = perf_counter_ns()
        print(response1(decoupe(lines)))
        m = perf_counter_ns()
        print(f"Réponse en {(m - s) / 1000}ms.")
        print(response2(decoupe(lines)))
        e = perf_counter_ns()
        print(f"Réponse en {(e - m) / 1000}ms.")
        f.close()
