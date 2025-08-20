
user_unit1 = int(input("Enter The Unit range 1: " ))

if 0 <= user_unit1 <= 100:
    price = user_unit1 * 1
    print(f"The range of unit is 0 to 100 so price: {price}")
    
elif user_unit1 > 101 and user_unit1 <= 200:
    calc_1= 100 * 1
    calc2 = user_unit1 - 100
    calc3 = calc2 * 2
    total_price = calc_1 + calc3
    print(f"The range of unit is 101 to 200 so the price is : {total_price}")

elif user_unit1 > 201 and user_unit1 <= 300:
    calc_1 = 100 * 1
    calc_2 = 100 * 2
    calc2 = user_unit1 - 200
    calc3 = calc2 * 3
    total_price = calc_1 + calc_2 + calc3
    print(f"The range of unit is 201 to 300 so the price is : {total_price}")

elif user_unit1 > 301 and user_unit1 <= 400:
    calc_1 = 100 * 1
    calc_2 = 100 * 2
    calc_3 = 100 * 3
    calc2 = user_unit1 - 300
    calc3 = calc2 * 4
    total_price = calc_1 + calc_2 + calc_3 + calc3
    print(f"The range of unit is 101 to 200 so the price is : {total_price}")

elif user_unit1 > 401:
    calc_1 = 100 * 1
    calc_2 = 100 * 2
    calc_3 = 100 * 3
    calc_4 = 100 * 4
    calc2 = user_unit1 - 400
    calc3 = calc2 * 5
    total_price = calc_1 + calc_2 + calc_3 + calc_4 + calc3
    print(f"The range of unit is 101 to 200 so the price is : {total_price}")

else:
    print("Somthing happening......")

