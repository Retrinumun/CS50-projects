towel = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
if towel == "42":
    print("Yes")
elif towel == "forty two":
    print("Yes")
elif towel == "forty-two":
    print("Yes")
else:
    print("No")