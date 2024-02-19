import random as rd


def create_groups(names: list[str], n: int) -> list[list[str]] | None:
    if len(names) < n:
        return None

    groups = [[] for _ in range(n)]

    rd.shuffle(names)

    for i, name in enumerate(names):
        groups[i % n].append(name)

    return groups
