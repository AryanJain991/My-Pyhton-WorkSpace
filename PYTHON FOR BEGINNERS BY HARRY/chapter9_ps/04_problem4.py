
with open("text.txt", "r") as f:
    content = f.read().lower()

if "####" in content:
    contentnew = content.replace("####", "donkey")
    
    with open("text.txt","w") as f:
        f.write(contentnew)

    print("The word #### is replaced")

else:
    print("The word #### is not present in the text file")