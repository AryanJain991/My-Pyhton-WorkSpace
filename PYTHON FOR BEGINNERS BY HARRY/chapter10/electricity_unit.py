user_unit1 = int(input("Enter The Unit range 1: " ))

if 0 <= user_unit1 <= 100:
    price = user_unit1 * 1
    print(f"The range of unit is 0 to 100 so price: {price}")

elif 101 <= user_unit1 <= 200:
    price = (user_unit1 * 1) + (user_unit1 * 2)
    print(f"The range of unit is 101 to 200 so price: {price}")

elif 201 <= user_unit1 <= 300:
    price = (user_unit1 * 1) + (user_unit1 * 2) + (user_unit1 * 3)
    print(f"The range of unit is 201 to 300 so price: {price}")

elif 301 <= user_unit1 <= 400:
    price = (user_unit1 * 1) + (user_unit1 * 2) + (user_unit1 * 3) + (user_unit1 * 4)
    print(f"The range of unit is 301 to 400 so price: {price}")

elif user_unit1 < 400:
    price = (user_unit1 * 1) + (user_unit1 * 2) + (user_unit1 * 3) + (user_unit1 * 4) + (user_unit1 * 5)
    print(f"The range of unit is 401 to 500 and above so price: {price}")

else:
    print("Program is succesfull done")

