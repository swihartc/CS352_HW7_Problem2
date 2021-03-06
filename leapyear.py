
def leap_year():
    pass

def valid_input(x):
    if type(x) != int:
        return None
    elif x < 0:
        return None
    return x


if __name__ == '__main__':
    leapyear()