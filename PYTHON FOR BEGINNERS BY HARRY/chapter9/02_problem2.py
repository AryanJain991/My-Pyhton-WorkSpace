# f = open("aj.txt", "r")
# lines = f.readlines()
# print(lines)
# f.close()

f = open(r"aj.txt", "r")

lines = f.readline()
while(lines != ""):
    print(lines)
    lines = f.readline()

f.close()