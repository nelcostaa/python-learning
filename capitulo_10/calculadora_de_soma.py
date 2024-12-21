while True:
    try:
        num_1 = input("Digite um numero: (enter 'q' to quit) ")
        if num_1 == "q":
            break
        num_1 = int(num_1)

        num_2 = input("Digite um numero (enter 'q' to quit) ")
        if num_2 == "q":
            break
        num_2 = int(num_2)
    except ValueError:
        print("Porfavor insira apenas numeros! Obrigado :)")
    else:
        soma = num_1 + num_2
        print(f"A soma do valor inserido e: {soma}\n")
