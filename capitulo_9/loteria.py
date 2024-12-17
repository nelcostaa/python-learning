from random import choice

numeros_e_letras = (12, 43, 23, 54, 34, 21, 27, "a", "b", "j", "h")

ticket_premiado = []

while len(ticket_premiado) < 4:
    escolha = choice(numeros_e_letras)

    if escolha not in ticket_premiado:
        ticket_premiado.append(escolha)


print("Qual ticket que corresponda aos numeros e letras abaixo, ganhou!")
print(ticket_premiado)
