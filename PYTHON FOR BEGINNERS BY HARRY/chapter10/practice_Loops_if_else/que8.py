# Question 8: Write a program to check if a year entered by the user is a leap year or not.
year = int(input("Pls Enter The Year: "))

if year % 4 == 0:
    print(f"Entered year {year} Is a Leap Year ")

else:
    print(f"{year} is Not a Leap Year")