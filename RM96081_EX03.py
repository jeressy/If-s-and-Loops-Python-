m_impar= 0
m_par= 0

print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES\n')
for impar in range (1,51,2):
    if impar >= 0:
       m_impar += float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {impar}: "))

total_m_impar = float(m_impar/ 25)

print(f'A média dos alunos de número ímpar é de: {total_m_impar:.2f}')

print('\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES\n')
for par in range (2,51,2):
    if par >= 0:
        m_par += int(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {par}: "))

total_m_par = float(m_par/ 25)
print(f'A média dos alunos de número ímpar é de: {total_m_par:.2f}')

m_turmas = [total_m_par, total_m_impar]
maior = max(m_turmas)


if total_m_par == total_m_impar:
    print('\nAs turmas possuem médias iguais.')
elif total_m_impar == maior:
    print( '\nA turma com os alunos de números ÍMPARES possui a maior média.')
elif total_m_par == maior:
    print('\nA turma com os alunos de números PARES possui a maior média.')
