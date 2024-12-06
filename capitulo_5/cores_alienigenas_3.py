alien_color = input("Qual a cor do alien?")

if alien_color.lower() == "verde":
    print("You won 5 points")
elif alien_color.lower() == "vermelho":
    print("You won 10 points")
else:
    print("You won 15 points")
