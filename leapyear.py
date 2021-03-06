


def valid_input(x):
    if type(x) != int:
        return None
    elif x < 0:
        return None
    return x

def div_400(x):
    if x % 400 == 0:
        return True
    return False

def div_100(x):
    if x % 100 == 0:
        return True
    return False

def div_4(x):
    if x % 4 == 0:
        return True
    return False

def leap_year(x):
    if div_400(x) or (div_4(x) and not div_100(x)):
        return True
    return False

if __name__ == '__main__':
    x = None
    while True:
        x = input("Enter a year: ")
        if valid_input(x) != None:
            break
        print("Invalid Input. Try again")
    if leap_year(x):
        print("Is a leap year")
    else:
        print("Not a leap year")