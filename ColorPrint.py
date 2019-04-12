from __future__ import print_function


try:
    import __builtin__
except ImportError:  # Python 3
    import builtins as __builtin__

RED = '\u001b[38;5;196m'
BLUE = '\u001b[38;5;12m'
GREEN = '\u001b[38;5;46m'
YELLOW = '\u001b[38;5;220m'
CYAN = '\u001b[38;5;51m'
PINK = '\u001b[38;5;213m'
MAGENTA = '\u001b[38;5;163m'
OLIVE = '\u001b[38;5;100m'
GRAY = '\u001b[38;5;240m'
DARKGRAY = '\u001b[38;5;235m'
RESET = '\u001b[0m'
COLORS = [RED, BLUE, GREEN, YELLOW, CYAN, PINK, MAGENTA, OLIVE, GRAY, DARKGRAY, RESET]

def print(s='', color='default'):
    s = str(s)

    if color in ['default', 'black', 'k']:
        s = RESET + s
    elif color in ['blue', 'b']:
        s = BLUE + s
    elif color in ['cyan', 'c']:
        s = CYAN + s
    elif color in ['gray', 'grey']:
        s = GRAY + s
    elif color in ['darkgrey', 'darkgray']:
        s = DARKGRAY + s
    elif color in ['green', 'g']:
        s = GREEN + s
    elif color in ['magenta', 'm']:
        s = MAGENTA + s
    elif color in ['red', 'r']:
        s = RED + s
    elif color in ['yellow', 'y']:
        s = YELLOW + s
    elif color in ['pink']:
        s = PINK + s
    elif color in ['olive', 'o']:
        s = OLIVE + s
    elif color in ['random', 'rand']:
        from random import choice
        s = choice(COLORS) + s
    elif color in ['discrete_random', 'drand']:
        from random import choice
        s = ''.join(list(map(lambda x: choice(COLORS) + x + RESET, s)))
    else:
        raise TypeError
    s += RESET
    return __builtin__.print(s)


if __name__ == '__main__':
    print(' '.join([C + str(i) + RESET for i, C in enumerate(COLORS)]))
