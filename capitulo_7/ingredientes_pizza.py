pizza = []

prompt = "Digite o ingrediente que voce deseja adicionar a pizza"
prompt += "\n(Digite quit para encerrar.) "

ingrediente = ""

while ingrediente != "quit":
    ingrediente = input(prompt)

    if ingrediente != "quit":
        pizza.append(ingrediente)
