def print_formatted(number):
    w = len(bin(number)[2:])
    for x in range(1,number+1):
        print(f"{x:{w}d} {x:{w}o} {x:{w}X} {x:{w}b}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)