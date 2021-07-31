def print_formatted(x):
    """Our task is print the string in a formatted way
    - Decimal
    - Octal
    - Hexadecimal
    - Binary
    Now the condition was to make sure the letters are in uppercase

    Args:
        x (string): In this way we can apply string functions
    """
    space = len(bin(x)[2:])
    for i in range(1,x+1):
        print(str(i).rjust(space, ' '), oct(i)[2:].rjust(space, ' ').upper(), hex(i)[2:].rjust(space, ' ').upper(), bin(i)[2:].rjust(space, ' ').upper())

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)