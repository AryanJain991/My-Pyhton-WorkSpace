
for i in range(1,51):
    count = 0
    for j in range(1, 1+i):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f"Prime Number is: {i}")