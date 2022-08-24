with_vowels = input("What would you like to say? ").strip()

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

new_str = ""

for vowel in with_vowels:
    if vowel not in vowels:
            new_str += vowel
print(new_str)


