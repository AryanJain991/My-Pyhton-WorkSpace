# str = "Hey I am Aryan and what's your name"

# f = open("myfile.txt", "w")

# f.write(str)

# f.close()

# with open("poem.txt", "r") as f:
#     content = f.read().lower()
#     if("twinkle" in content):
#         print("The Word twinkle present in the content")

#     else:
#         print("The Word twinkle is not present in the content")




f = open("myfile.txt", "r")
lines = f.readlines()
print(lines)
f.close()
