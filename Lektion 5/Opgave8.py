from typing import List


def kvadrat(x: float) -> str:
    return str(x*x)


print('Resultatet er: ' + kvadrat(9))

print('----------------------------------------------------------')


listen = [1, 2, 3, 4]


def minsum(liste: List[int]) -> str:
    return str(sum(liste))


print(minsum(listen))

print('-----------------------------------------------------------')


listen2 = ['Christian', 'Anel', 'Allan']

"""print(minsum(listen2))"""

