from typing import Generator
from time import perf_counter_ns


def response1(_lines: str) -> str:
    for i, c in enumerate(_lines):
        if i < 3: continue
        q: str = _lines[i-3:i+1]
        if q[0] != q[1] and q[0] != q[2] and q[0] != q[3]:
            if q[1] != q[2] and q[1] != q[3]:
                if q[2] != q[3]:
                    return f"Réponse 1 : {i+1}"


def response2(_lines: str) -> str:
    for i, c in enumerate(_lines):
        if i < 13: continue
        q: str = _lines[i-13:i+1]
        for j, d in enumerate(q):
            if q.find(d, j+1) > -1:
                break
        else:
            return f"Réponse 1 : {i + 1}"


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines: list[str] = f.read().splitlines()

        print(f"Longueur du fichier {len(lines)} lignes.")
        s = perf_counter_ns()
        print(response1(lines[0]))
        m = perf_counter_ns()
        print(f"Réponse en {(m - s) / 1000}ms.")
        print(response2(lines[0]))
        e = perf_counter_ns()
        print(f"Réponse en {(e - m) / 1000}ms.")
        f.close()
