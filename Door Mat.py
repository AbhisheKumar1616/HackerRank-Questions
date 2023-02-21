if __name__ == "__main__":
    n, m = map(int, input().split())
    mat1 = ""
    for i in range(n // 2):
        mat1 += (".|." * (i * 2 + 1)).center(m, "-") + "\n"

    print(mat1 + "WELCOME".center(m, "-") + mat1[::-1])


#_______________________________________________________________________________________________________________________

inp=input().split(" ")
l=int(inp[0])
b=int(inp[1])
#top part
for a in range(1,l,2):
   print((".|."*a).center(b,"-"))
#middle part
print("WELCOME".center(b,"-"))
#bottom part
for a in reversed(range(1,l,2)):
   print((".|."*a).center(b,"-"))