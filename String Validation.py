if __name__ == '__main__':
    s = input()
    list_of_commands = ["isalnum()", "isalpha()", "isdigit()", "islower()", "isupper()"]
    for i in list_of_commands:
        # note: the question asks if s has any characters that math each function
        one_line_command = f'any(a.{i} for a in s)'
        print(eval(one_line_command))


#_______________________________________________________________________________________________________________________

if __name__=="__main__":
    s=input()
    print(any(s.isalnum() for s in s))
    print(any(s.isalpha() for s in s))
    print(any(s.isnumeric() for s in s))
    print(any(s.islower() for s in s))
    print(any(s.isupper() for s in s))