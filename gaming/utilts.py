
def validate_non_negative(number):
    if number < 0:
        raise ValueError('It must be non negative')
    return number


def validate_isalpha(string):
    if not string.isalpha():
        raise ValueError('it must be consist only letters')
    return string
