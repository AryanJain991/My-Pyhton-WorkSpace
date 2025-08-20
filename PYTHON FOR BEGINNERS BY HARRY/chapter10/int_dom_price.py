
age = int(input("please Enter Your Age: "))
flight_type = input("Please Write Flight Type international/domestic: ").lower()

if age < 25:
    if flight_type == "international":
        price = 5000
        print(f"Flight Type is International so the price is: {price}Rs.")

    elif flight_type == "domestic":
        price = 3000
        print(f"Flight Type is Domestic so the price is: {price}Rs.")
    
    else:
        print("Pls Write Correct Type")

elif age > 25:
    if flight_type == "international":
        price = 11000
        print(f"Flight Type is International so the price is: {price}Rs.")

    elif flight_type == "domestic":
        price = 7000
        print(f"Flight Type is Domestic so the price is: {price}Rs.")
    
    else:
        print("Pls Write Correct Type")

else:
    print("something wrong pls check your code")