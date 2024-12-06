prompt = "Digite quantos anos voce tem para calcularmos o valor do ingresso"
prompt += "\n(digite 'quit' para encerrar) "

while True:
    age = input(prompt)
    if age == "quit":
        break

    age = int(age)
    if age < 3:
        print("ingresso gratuito!")
    elif (age >= 3) and (age <= 12):
        print("o ingresso custa 10R$")
    elif age > 12:
        print("o ingresso custa 15R$")
