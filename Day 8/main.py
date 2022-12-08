import sys

from time import perf_counter_ns
# from pprint import pprint


def left(_lines: list[list], i: int, j: int, maxi: int) -> bool:
    if i < 0:
        return True
    if _lines[j][i] < maxi:
        return left(_lines, i-1, j, maxi)
    return False


def right(_lines: list[list], i: int, j: int, maxi: int) -> bool:
    if i >= len(_lines[j]):
        return True
    if _lines[j][i] < maxi:
        return right(_lines, i+1, j, maxi)
    return False


def up(_lines: list[list], i: int, j: int, maxi: int) -> bool:
    if j < 0:
        return True
    if _lines[j][i] < maxi:
        return up(_lines, i, j-1, maxi)
    return False


def down(_lines: list[list], i: int, j: int, maxi: int) -> bool:
    if j >= len(_lines):
        return True
    if _lines[j][i] < maxi:
        return down(_lines, i, j+1, maxi)
    return False


def count_left(_lines: list[list], i: int, j: int, maxi: int) -> int:
    if i < 0:
        return 0
    if _lines[j][i] < maxi:
        return count_left(_lines, i-1, j, maxi) + 1
    return 1


def count_right(_lines: list[list], i: int, j: int, maxi: int) -> int:
    if i >= len(_lines[j]):
        return 0
    if _lines[j][i] < maxi:
        return count_right(_lines, i+1, j, maxi) + 1
    return 1


def count_up(_lines: list[list], i: int, j: int, maxi: int) -> int:
    if j < 0:
        return 0
    if _lines[j][i] < maxi:
        return count_up(_lines, i, j-1, maxi) + 1
    return 1


def count_down(_lines: list[list], i: int, j: int, maxi: int) -> int:
    if j >= len(_lines):
        return 0
    if _lines[j][i] < maxi:
        return count_down(_lines, i, j+1, maxi) + 1
    return 1


def response1(_lines: list[list]) -> str:
    somm: int = 0
    for j, row in enumerate(_lines):
        for i, col in enumerate(row):
            if left(_lines, i-1, j, col) or right(_lines, i+1, j, col) or \
               up(_lines, i, j-1, col) or down(_lines, i, j+1, col):
                somm += 1
    return f"Réponse 1 : Nombre total d'arbres visibles {somm}."


def response2(_lines) -> str:
    maxi: int = 0
    for j, row in enumerate(_lines):
        for i, col in enumerate(row):
            score: int = count_left(_lines, i-1, j, col) * count_right(_lines, i+1, j, col) * \
               count_up(_lines, i, j-1, col) * count_down(_lines, i, j+1, col)
            if score > maxi:
                maxi = score
    return f"Réponse 2 : Meilleur score {maxi}"


if __name__ == '__main__':
    lines: list[list] = []
    for li in sys.stdin.read().splitlines():
        lines.append([int(m) for m in li])

    print(f"Longueur du fichier {len(lines)} lignes.")
    s = perf_counter_ns()
    print(response1(lines))
    m = perf_counter_ns()
    print(f"Réponse en {(m - s) / 1000}ms.")
    print(response2(lines))
    e = perf_counter_ns()
    print(f"Réponse en {(e - m) / 1000}ms.")
