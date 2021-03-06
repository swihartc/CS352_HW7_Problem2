
def leap_year():
    pass

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
    pass


if __name__ == '__main__':
    while True:
        x = input("Enter a year: ")
        if valid_input(x) != None:
            break
        print("Invalid Input. Try again")