camel_case = input("Give a camelCase example: ")

for upper in camel_case:
    if upper.isupper() == True:
        print(f"_{upper.lower()}", end='')
    else:
        print(upper, end="")
    
print()
