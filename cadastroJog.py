
jogador = {}
lista = []
gol = []

while True:
  jogador['nome'] = str(input('Nome do jogador: '))
  #jogador['gols'] = gol
  partida = int(input('Quantas partidas ele jogou: '))
  jogador['part'] = partida
  soma = 0
  for i in range(0, partida):
    gol.append(int(input(f'Quantos gols o jogador {jogador["nome"]} marcou na partida {i}: ')))
  con = str(input('Deseja continuar[S/N]: ')).upper()
  jogador['gols'] = gol[:]
  gol.clear()
  lista.append(jogador.copy())
  if con == 'N':
    break


print('-='*35)
print(f'{"Nº":<5}{"Nome":<20}{"Gols"}')
for i, v in enumerate(lista):
  print(f'{i:<3} jogador {v["nome"]:<10}{v["gols"]}')
print('-='*35)
id = 0
while id != 999:
  id = int(input('Mostrar dados de qual jogador? (999 para parar): '))
  for i, v in enumerate(lista):
    if i == id:
      print(f'--LEVANTAMENTO DO JOGADOR {v["nome"]}')
      for i, v in enumerate(lista[id]['gols']):
        print(f'Na partida {i} marcou {v}!')