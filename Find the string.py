def count_substring(string, sub_string):
    c = 0
    a = len(sub_string) - 1
    for i in range(a, len(string)):
        s = string[i - a:i + 1]
        if s == sub_string:
            c += 1
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)