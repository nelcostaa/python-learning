pessoas = []

person = {
    "first_name": "Nelson",
    "last_name": "Costa",
    "age": 22,
    "city": "Curitiba",
}

person_2 = {
    "first_name": "andre",
    "last_name": "balbino",
    "age": 24,
    "city": "Sao Jose dos Campos",
}

person_3 = {
    "first_name": "Fafael",
    "last_name": "Moreira",
    "age": 23,
    "city": "Curitiba",
}

pessoas.append(person)
pessoas.append(person_2)
pessoas.append(person_3)

for person in pessoas:
    full_name = f'{person["first_name"]} {person["last_name"]}'
    location = person["city"]
    age = person["age"]
    print(f"{full_name.title()} has {age} years and lives in {location}")
