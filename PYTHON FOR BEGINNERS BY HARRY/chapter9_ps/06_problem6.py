with open ("log.txt") as f:
    content = f.read()

    if "python" in content.lower():
            print("the python word is present in the log file")
    else:
        print("The Word python is not found in the log file")