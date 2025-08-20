words = ["donkey", "bad", "ganda"]


with open("text.txt", "r") as f:
    content = f.read().lower()

for word in words:
    content = content.replace(word, "#" * len(word))
    
with open("text.txt","w") as f:
        f.write(content)