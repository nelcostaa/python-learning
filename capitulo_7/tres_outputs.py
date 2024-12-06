# Forma 1 - usando active para encerrar o programa
#
# prompt = "Digite quantos anos voce tem para calcularmos o valor do ingresso"
# prompt += "\n(digite 'quit' para encerrar) "
#
# active = True
# while active:
#     age = input(prompt)
#     if age == "quit":
#         active = False
#
#     age = int(age)
#     if age < 3:
#         print("ingresso gratuito!")
#     elif (age >= 3) and (age <= 12):
#         print("o ingresso custa 10R$")
#     elif age > 12:
#         print("o ingresso custa 15R$")

prompt = "Digite quantos anos voce tem para calcularmos o valor do ingresso"
prompt += "\n(digite 'quit' para encerrar) "

age = input(prompt)
while age != "quit":
    age = int(age)
    if age < 3:
        print("ingresso gratuito!")
    elif (age >= 3) and (age <= 12):
        print("o ingresso custa 10R$")
    elif age > 12:
        print("o ingresso custa 15R$")

    age = input(prompt)
