input = ['0', '0', '#', '1', '0', '0']

def start(head):
    while (input[head] == 'e' and head < len(input)):
        show(head, 'start')
        head += 1
    if (input[head] == '0' and head < len(input)):
            show(head, 'start')
            input[head] = 'e'
            head += 1
            S0(head)
    elif (input[head] == '1'):
        show(head, 'start')
        input[head] = 'e'
        head += 1
        S1(head)
    elif (input[head] == '#'):
        show(head, 'start')
        head += 1
        print("x is a subsequence of y")

def S0(head):
    while ((input[head] == '0' or input[head] == '1') and head < len(input)):
        show(head, 'S0')
        head += 1
    if (input[head] == '#'):
        show(head, 'S0')
        head += 1
        S0Y(head)

def S1(head):
    while ((input[head] == '0' or input[head] == '1') and head < len(input)):
        show(head, 'S1')
        head += 1
    if (input[head] == '#'):
        show(head, 'S1')
        head += 1
        S1Y(head)

def S0Y(head):
    while ((input[head] == '1' or input[head] == 'x') and head < len(input)-1):
        show(head, 'S0Y')
        input[head] = 'x'
        head += 1
    if (input[head] == '0'):
        show(head, 'S0Y')
        input[head] = 'x'
        head -= 1
        back(head)
    elif head == len(input)-1:
        print("x is not a subsequence of y")

def S1Y(head):
    while ((input[head] == '0' or input[head] == 'x') and head < len(input) - 1):
        show(head, 'S1Y')
        input[head] = 'x'
        head += 1
    if (input[head] == '1'):
        show(head, 'S1Y')
        input[head] = 'x'
        head -= 1
        back(head)
    elif head == len(input)-1:
        print("x is not a subsequence of y")

def back(head):
    while ((input[head] == '0' or input[head] == '1' or input[head] == 'x' or input[head] == '#') and head < len(input)):
        show(head, 'back')
        head -= 1
    if (input[head] == 'e'):
        show(head, 'back')
        head += 1
        start(head)

def show(head, state):
    config = input.copy()
    config.insert(head, state)
    print(config)

start(0)