
jogador = {}
gol = []

jogador['nome'] = str(input('Nome do jogador: '))
jogador['gols'] = gol
partida = int(input('Quantas partidas ele jogou: '))
jogador['part'] = partida
soma = 0
for i in range(0, partida):
  gol.append(int(input(f'Quantos gols o jogador {jogador["nome"]} marcou na partida {i}: ')))


for i in range(0, len(gol)):
  soma += gol[i]
jogador['total'] = soma
print(f'{jogador}')
print('-='*35)
print(f'O campo nome tem o valor {jogador["nome"]}')
print(f'O campo gols tem o valor {jogador["gols"]}')
print(f'O campo total tem o valor {jogador["total"]}')
print('-='*35)
print(f'O jogador {jogador["nome"]} jogou {jogador["part"]} partidas.')
for i, v in enumerate(jogador['gols']):
  print(f'=> Na partida {i}, fez {v} ')