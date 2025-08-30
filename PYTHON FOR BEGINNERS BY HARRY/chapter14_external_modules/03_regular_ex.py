import re
text = "The Name Of Puppy is Jerrycho He is a trained soldier puppy"

# Search For a pattern
# match = re.search("is",text)

# if match:
#     print("Match is found")
#     print(f"First Index is: {match.start()}")
#     print(f"end Index is: {match.end()}")

# matches = re.findall("is",text,re.IGNORECASE)   #case insensitive search for lower case and upper case both

# print("matches: ", matches)

change_text = re.sub("Puppy","German Shepard", text, flags=re.IGNORECASE)
print("new_text_is: ",change_text)  