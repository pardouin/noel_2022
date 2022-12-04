from random import choice
from itertools import permutations

participants = ['Anne', 'Benjamin', 'Elsa', 'Eric', 'Laure', 'Maria', 'Nicolas', 'Pierre', 'Sarah']
n = len(participants)

couples = {('Anne', 'Benjamin'),
           ('Elsa', 'Nicolas'),
           ('Eric', 'Maria'),
           ('Pierre', 'Sarah')}

perm = [p for p in permutations(participants)
        if all((*sorted((p[k-1], p[k])),) not in couples for k in range(n))]

p = choice(perm)

for k in range(n):
    a, b = p[k-1], p[k]
    with open(f'{a}.txt', 'w') as fichier:
        fichier.write(f'{a} offre un cadeau a {b}')