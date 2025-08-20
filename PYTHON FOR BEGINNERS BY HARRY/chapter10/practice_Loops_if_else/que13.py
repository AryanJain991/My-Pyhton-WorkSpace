# # Quetion 13 - Write a program to check whether a character entered by the user is a vowel or a consonant. 

# char = input("Please Enter The Single Character To Check It is Vowel or Consonant: ")

# consonants = tuple(("B", "C" ,"D", "F" ,"G" ,"H" ,"b" ,"c" ,"d" ,"f" ,"g" ,"h"))
# vowels = tuple(("A", "E", "I", "O", "U", "a", "e", "i", "o", "u"))

# if char in consonants :
#     print(f"{char} Is Consonants")

# elif char in vowels:
#     print(f"{char} is Vowel")

# else:
#     print(f"Not Defined")

char = input("Please Enter a Single Alphabet Character: ")

# Check if the input is a single alphabet letter
if char.isalpha() :
    vowels = "aeiouAEIOU"
    
    if char in vowels:
        print(f"{char} is a Vowel")
    else:
        print(f"{char} is a Consonant")
else:
    print("❌ Invalid input. Please enter a single alphabet character.")
