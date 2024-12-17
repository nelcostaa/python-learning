from random import choice


def criar_ticket_aleatorio(alternativas):
    """Preenche um ticket de loteria com numeros sorteados de uma lista"""
    ticket = []
    while len(ticket) < 4:
        escolha = choice(alternativas)

        if escolha not in ticket:
            ticket.append(escolha)

    return ticket


def checar_ticket(ticket_premiado, ticket_aleatorio):
    """Checa se o ticket premiado e igual ao aleatorio"""
    for elemento in ticket_premiado:
        if elemento not in ticket_aleatorio:
            return False

    return True


numeros_e_letras = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "j", "h"]
ticket_premiado = criar_ticket_aleatorio(numeros_e_letras)

tentativa = 0
vitoria = False

while not vitoria:
    ticket_tentativa = criar_ticket_aleatorio(numeros_e_letras)
    vitoria = checar_ticket(ticket_premiado, ticket_tentativa)
    tentativa += 1

print(f"Foram realizadas {tentativa} tentativas")
print(f"ticket aleatorio: {ticket_tentativa}")
print(f"ticket premiado: {ticket_premiado}")
