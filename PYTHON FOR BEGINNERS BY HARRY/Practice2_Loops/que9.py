
originial_num = int(input("Pls Enter A number: "))
reversed_num = 0

while originial_num > 0:

    last_digit = originial_num % 10
    reversed_num = (reversed_num * 10) + last_digit
    originial_num = originial_num//10

print(f"The Reversed_num is: {reversed_num} ")