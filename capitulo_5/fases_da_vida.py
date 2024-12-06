age = int(input("Quantos anos voce tem? "))

if age < 2:
    print("You baby")
elif (age >= 2) and (age < 4):
    print("You child")
elif (age >= 4) and (age < 13):
    print("You boy!")
elif (age >= 13) and (age < 20):
    print("you teenager")
elif (age >= 20) and (age < 65):
    print("You adult! yiekes!!")
elif age >= 65:
    print("You old!")
