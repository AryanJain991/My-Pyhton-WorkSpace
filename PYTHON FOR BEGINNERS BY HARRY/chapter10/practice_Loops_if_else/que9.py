''' Question 9: Write a program to grade a student based on their marks. Use the following criteria:
Marks >= 90: Grade A
Marks >= 80: Grade B
Marks >= 70: Grade C
Marks >= 60: Grade D
Marks < 60: Fail '''

Marks = input("Pls Enter The Marks: ")
try:
    var = int(Marks)
except ValueError:
    var = float(Marks)

if var >= 90:
    print(f"You Got {var} Marks Which Is 90 Above or Equal So Your Grade Is: A ")

elif 80 <= var < 90:
    print(f"You Got {var} Marks So Your Grade is: B")

elif 70 <= var < 80:
    print(f"You Got {var} Marks So Your Grade is: C")

elif 60 <= var < 70:
    print(f"You Got {var} Marks So Your Grade is: D")

else:
    print("You Are Fail\nTry Next Year")