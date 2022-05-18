from random import randint
from time import sleep
from operator import itemgetter

j = {
'Jogador1': randint(1, 6),
'Jogador2': randint(1, 6),
'Jogador3': randint(1, 6),
'Jogador4': randint(1, 6)}
#j.sort()
rank = ()

for jj, v in j.items():
  print(f'{jj} jogou {v}')
  sleep(1)
rank = sorted(j.items(), key = itemgetter(1), reverse=True)
#print(rank)
for i, v in enumerate(rank):
  
  print(f'{i+1}º lugar {v[0]} jogou {v[1]}')
  sleep(0.5)