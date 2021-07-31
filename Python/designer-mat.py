def solution(row, column):
    """For solving the designer mat problem we need a
    row and column values

    Args:
        row ([int]): [description]
        column ([int]): [description]
    """
    dash = '-'
    special_char = '.|.'
    word = 'WELCOME'
    midValue = (row + 1)//2 # Our row value is odd so by taking its we want to have an integer value
    for i in range(1, row+1):
        if (i<midValue):
            print(dash.rjust(((column - 3*(2*i-1))//2), dash) + special_char*(2*i - 1) + dash.ljust(((column - 3*(2*i-1))//2), dash))
        elif (i>midValue):
            print(dash.rjust(((column - 3*(2*(row - i)+1))//2), dash) + special_char*(2*(row - i)+1) + dash.ljust(((column - 3*(2*(row - i)+1))//2), dash))
        else:
            print(dash.rjust(((column - 7)//2), dash) + word + dash.ljust(((column - 7)//2), dash))
    return

if __name__ == '__main__':
    N,M = map(int, input().split())
    solution(row=N, column=M)