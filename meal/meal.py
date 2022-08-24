def main():
    hours, minutes = input("What time is it? ").strip().split(":")

    hours = int(hours)
    minutes = convert(minutes)

    if hours == 7 and minutes < .99:
        print("breakfast time")
    elif hours == 8 and minutes == .00:
        print("breakfast time")
    elif hours == 12 and minutes < .99:
        print("lunch time")
    elif hours == 13 and minutes == .00:
        print("lunch time")
    elif hours == 18 and minutes < .99:
        print("dinner time")
    elif hours == 19 and minutes == .00:
        print("dinner time")


def convert(time):
    time = float(time)/60
    return time




if __name__ == "__main__":
    main()