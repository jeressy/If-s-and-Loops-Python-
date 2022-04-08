print(f'Bem-vindo(a)!\n Níveis de assinatura:')

rank = int(input('1- Basic \n2- Silver \n3- Gold \n4- Platinum \nInforme o nível do cliente (digite APENAS o número): '))
if rank == 1:
    bonus = float(input(f'Clientes "Basic" pagam 30% do bônus.\n\nPor favor, insira o rendimento anual do cliente: R$'))
    bonus = bonus / 100
    print(f'O cliente vai pagar R${bonus * 30:.2f}')

elif rank == 2:
    bonus = float(input(f'Clientes "Silver" pagam 20% do bônus.\n\nPor favor, insira o rendimento anual do cliente: R$'))
    bonus = bonus / 100
    print(f'O cliente vai pagar R${bonus * 20:.2f}')

elif rank == 3:
    bonus = float(input(f'Clientes "Gold" pagam 10% do bônus.\n\nPor favor, insira o rendimento anual do cliente: R$'))
    bonus = bonus / 100
    print(f'O cliente pagará R${bonus * 10:.f}')

elif rank == 4:
    bonus = float(input(f'Clientes "Platinum" pagam 5% do bônus.\n\nPor favor, insira o rendimento anual do cliente: R$'))
    bonus = bonus / 100
    print(f'O cliente pagará R${bonus * 5:.f}')

else:
    print('\nDigite um número válido.')



