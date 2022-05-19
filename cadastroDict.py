
pessoa = {}
lista = []
med = 0

while True:
  pessoa['nome'] = str(input('Nome: '))
  sex = str(input('Sexo [M/F]: ')).upper()
  if sex == 'M' or sex == 'F':
    pessoa['sexo'] = sex
  else:
    while True:
      sex = str(input('ERRO! Sexo [M/F]: ')).upper()
      if sex in 'MF':
        pessoa['sexo'] = sex
        break
  pessoa['idade'] = int(input('Idade: '))
  cont = str(input('Deseja continuar [S/N]: ')).upper()
  lista.append(pessoa.copy())
  if cont == 'N':
    break

#print(lista)
print(f'A) Foram cadastradas {len(lista)}')
for i in lista:
  med += i['idade']
print(f'B) A média de idade é {med/len(lista)} anos')
print(f'C) As mulheres cadastradas são: ', end = '')
for i in lista:  
  if i['sexo'] == 'F':
    print(f'{i["nome"]} ', end = '')
print()
print(f'D) As pessoas acima da média são:')
for n in lista:
  if n['idade'] > med/len(lista):
    print(f'nome = {n["nome"]}; sexo = {n["sexo"]}; idade = {n["idade"]}')
      