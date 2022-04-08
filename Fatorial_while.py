
minuto = int(input("Digite o minuto atual: "))

conta = 1
senha = 1

while conta <= minuto:
    senha *= conta
    conta += 1

print(f'A senha é "LIBERDADE{senha}"')
