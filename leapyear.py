
def leap_year():
    pass

def valid_input(x):
    if type(x) != int:
        return None
    elif x < 0:
        return None
    return x

def div_400(x):
    pass

def div_100(x):
    pass
def div_4(x):
    pass


if __name__ == '__main__':
    while True:
        x = input("Enter a year: ")
        if valid_input(x) != None:
            break
        print("Invalid Input. Try again")