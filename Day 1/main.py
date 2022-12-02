from typing import Generator
from time import perf_counter_ns


def elves(_lines: list) -> Generator:
    """Regroupe les valeurs de chaque colis de chaque elfe
    @type _lines: object
    """
    while True:
        try:
            i: int = _lines.index('')
            yield _lines[:i]
            _lines: list = _lines[i + 1:]
        except ValueError:
            yield _lines
            return


def sum_list(_l: list[str]) -> int:
    """Retourne la sum des nombre de la liste en convertissant les chaines en entier préalablement
    @type _l: list[str]
    """
    return sum([int(v) for v in _l])


def response1(groups: Generator) -> str:
    """Retourne le maximum porté par un elfe"""
    maxi: int = 0
    for grp in groups:
        _sum = sum_list(grp)
        if _sum > maxi:
            maxi = _sum
    return f"Le maximum de calories est {maxi}."


def response2(groups: Generator) -> str:
    """Retourne la somme des 3 elfes portant le plus"""
    sums = []
    for grp in groups:
        sums.append(sum_list(grp))
    sums.sort()
    return f"Calories cumulées des 3 elfes les plus chargés {sum(sums[-3:])}."


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines: list[str] = f.read().splitlines()
        print(f"{len(lines)} packetages sur des elfes.")
        s = perf_counter_ns()
        print(response1(elves(lines)))
        m = perf_counter_ns()
        print(f"Réponse en {(m-s)/1000}ms.")
        print(response2(elves(lines)))
        e = perf_counter_ns()
        print(f"Réponse en {(e-m)/1000}ms.")
        f.close()
