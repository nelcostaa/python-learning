def mostrar_mensagens(mensagens):
    """Imprime as mensagems de uma lista"""
    for mensagem in mensagens:
        print(mensagem)


def enviar_mensagens(mensagens_atuais, mensagens_enviadas):
    """Transfere os itens de uma lista para outra lista"""
    print("\nEnviando todas as mensagens:")
    while mensagens_atuais:
        current_message = mensagens_atuais.pop()
        print(current_message)
        mensagens_enviadas.append(current_message)


mensagens = ["ola mundo", "tchau mundo", "python e bom"]
mostrar_mensagens(mensagens)

mensagens_enviadas = []
enviar_mensagens(mensagens, mensagens_enviadas)

print("Listas finais:")
print(mensagens)
print(mensagens_enviadas)
