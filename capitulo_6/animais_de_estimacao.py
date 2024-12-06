animais = []

animal = {"tipo": "cachorro", "dono": "nelson"}

animais.append(animal)

animal = {"tipo": "gato", "dono": "rafael"}

animais.append(animal)

animal = {"tipo": "hamster", "dono": "andre"}

animais.append(animal)

for animal in animais:
    tipo_animal = animal["tipo"]
    dono_animal = animal["dono"]
    print(f"Esse {tipo_animal} e do {dono_animal.title()}")
