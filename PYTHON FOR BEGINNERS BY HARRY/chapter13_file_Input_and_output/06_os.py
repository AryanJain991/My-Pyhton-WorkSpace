import os

a = os.listdir("dir")

print(a)
print(os.getcwd())
print(os.path.exists("file.txt"))
#we can also remove file using os module

# os.remove("sample.txt")

os.rmdir("dir")
