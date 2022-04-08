print('Bem-vindo(a)! \nPor favor, digite a quantidade de votos para cada dia da semana.')

seg = int(input('Segunda-feira: '))
ter = int(input('Terça-feira: '))
qua = int(input('Quarta-feira: '))
qui = int(input('Quinta-feira: '))
sex = int(input('Sexta-feira: '))

semana = [seg, ter, qua, qui, sex]

print(f'\nQuantidade de votos:\nSegunda-feira: {seg} | Terça-feira: {ter}')
print(f'Quarta-feira: {qua} | Quinta-feira: {qui}\nSexta-feira: {sex}\n')

maior = max(semana)


if (seg == maior):
    print(f'O dia escolhido recebeu {maior} votos.')
    print('As lives acontecerão na segunda-feira!')

elif (ter == maior):
    print(f'O dia escolhido recebeu {maior} votos.')
    print('As lives acontecerão na terça-feira!')
elif (qua == maior):
    print(f'O dia escolhido recebeu {maior} votos.')
    print('As lives acontecerão na quarta-feira!')
elif (qui == maior):
    print(f'O dia escolhido recebeu {maior} votos.')
    print('As lives acontecerão na quinta-feira!')
else:
    print(f'O dia escolhido recebeu {maior} votos.')
    print('As lives acontecerão na sexta-feira!')



