
delivery_kilometer = int(input("Enter Kilometer: "))

if (0 < delivery_kilometer <= 7):
    price = 7 * 0
    print (f"delivery kilomter is uder 7 kilometer so the price is: {price}")

elif(delivery_kilometer > 7):
    calc_1 = delivery_kilometer - 7
    total_price = calc_1 * 2
    print (f"delivery kilomter is above 7 kilometer so the price is: {total_price}")

else:
    print("Something is Wrong pls check your program again")