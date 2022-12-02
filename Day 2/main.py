from typing import Generator
from time import perf_counter_ns


def decoupe(_lines: list) -> Generator:
    for line in _lines:
        op, pl = line.split(sep=' ')
        yield op, pl


def response1(_lines: Generator) -> str:
    score: int = 0
    for op, pl in _lines:
        match pl:
            case 'X':
                if op == "A":
                    score += 1 + 3
                elif op == "B":
                    score += 1
                else:
                    score += 1 + 6
            case 'Y':
                if op == "A":
                    score += 2 + 6
                elif op == "B":
                    score += 2 + 3
                else:
                    score += 2
            case 'Z':
                if op == "A":
                    score += 3
                elif op == "B":
                    score += 3 + 6
                else:
                    score += 3 + 3
    return f"Score final en application de toute la stratégie {score}."


def response2(_lines: Generator) -> str:
    score: int = 0
    for op, pl in _lines:
        match pl:
            case 'X':
                if op == "A":
                    score += 3 + 0
                elif op == "B":
                    score += 1 + 0
                else:
                    score += 2 + 0
            case 'Y':
                if op == "A":
                    score += 1 + 3
                elif op == "B":
                    score += 2 + 3
                else:
                    score += 3 + 3
            case 'Z':
                if op == "A":
                    score += 2 + 6
                elif op == "B":
                    score += 3 + 6
                else:
                    score += 1 + 6
    return f"Score final en application de toute la stratégie {score}."


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines: list[str] = f.read().splitlines()

        print(f"Longueur de la stratégie {len(lines)}")
        s = perf_counter_ns()
        print(response1(decoupe(lines)))
        m = perf_counter_ns()
        print(f"Réponse en {(m - s) / 1000}ms.")
        print(response2(decoupe(lines)))
        e = perf_counter_ns()
        print(f"Réponse en {(e - m) / 1000}ms.")
        f.close()
