try:
    num_1 = input("Digite um numero: ")
    num_1 = int(num_1)

    num_2 = input("Digite um numero: ")
    num_2 = int(num_2)
except ValueError:
    print("Porfavor insira apenas numeros! Obrigado :)")
else:
    soma = num_1 + num_2
    print(f"A soma do valor inserido e: {soma}")
