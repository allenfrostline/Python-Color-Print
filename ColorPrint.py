from __future__ import print_function


try:
    import __builtin__
except ImportError:  # Python 3
    import builtins as __builtin__


def print(s, color='default'):
    BLUE = '\u001b[38;5;12m'
    CYAN = '\u001b[38;5;51m'
    GRAY = '\u001b[38;5;240m'
    GREEN = '\u001b[38;5;46m'
    MAGENTA = '\u001b[38;5;163m'
    RED = '\u001b[38;5;196m'
    YELLOW = '\u001b[38;5;220m'
    RESET = '\u001b[0m'

    if color in ['default', 'black', 'k']:
        s = RESET + s
    elif color in ['blue', 'b']:
        s = BLUE + s
    elif color in ['cyan', 'c']:
        s = CYAN + s
    elif color in ['gray', 'grey']:
        s = GRAY + s
    elif color in ['green', 'g']:
        s = GREEN + s
    elif color in ['magenta', 'm']:
        s = MAGENTA + s
    elif color in ['red', 'r']:
        s = RED + s
    elif color in ['yellow', 'y']:
        s = YELLOW + s
    elif color in ['random', 'rand']:
        from random import choice
        s = choice([RESET, BLUE, CYAN, GRAY, GREEN, MAGENTA, RED, YELLOW]) + s
    elif color in ['discrete_random', 'drand']:
        from random import choice
        s = ''.join(list(map(lambda x: choice([RESET, BLUE, CYAN, GRAY, GREEN, MAGENTA, RED, YELLOW]) + x + RESET, s)))
    else:
        raise TypeError
    s += RESET
    return __builtin__.print(s)


if __name__ == '__main__':
    pass
