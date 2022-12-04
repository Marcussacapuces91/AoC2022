from typing import Generator
from time import perf_counter_ns


def decoupe(_lines: list) -> Generator:
    for line in _lines:
        a, b = line.split(',')
        yield int(a.split('-')[0]), int(a.split('-')[1]), int(b.split('-')[0]), int(b.split('-')[1])

        
def response1(_lines: Generator) -> str:
    sum: int = 0
    for aMin, aMax, bMin, bMax in _lines:
        if aMin <= bMin and aMax >= bMax or aMin >= bMin and aMax <= bMax:
            sum += 1
    return f"Resultat 1 : {sum}"


def response2(_lines: Generator) -> str:
    sum: int = 0
    for aMin, aMax, bMin, bMax in _lines:
       if aMin > bMax or aMax < bMin:
            pass
        else:
            min = aMax if aMax < bMax else bMax
            max = aMin if aMin > bMin else bMin
            sum += 1  
    return f"Resultat 2 : {sum}"


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines: list[str] = f.read().splitlines()

        print(f"Nombre de paires {len(lines)}")
        s = perf_counter_ns()
        print(response1(decoupe(lines)))
        m = perf_counter_ns()
        print(f"Réponse en {(m - s) / 1000}ms.")
        print(response2(decoupe(lines)))
        e = perf_counter_ns()
        print(f"Réponse en {(e - m) / 1000}ms.")
        f.close()
