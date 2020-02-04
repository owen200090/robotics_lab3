def validate_pin(x):
    if (x.isdigit() and (len(x) == 4 or len(x) == 6 )):

        return True

    return False

