def main():
    mood = input("")
    print(convert(mood))

def convert(moods):
    moody = moods.replace(":(","🙁").replace(":)", "🙂")
    return moody

main()

