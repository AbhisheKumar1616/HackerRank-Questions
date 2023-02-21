from sys import stdin


def spiralPrint(mat, n, m):
    rs,cs=0,0
    re,ce=n-1,m-1
    st=""
    count=0
    len_list=n*m
    while count!=len_list:
        for i in range(cs,ce+1):
            st=st+str(mat[rs][i])+" "
            count+=1
        rs+=1
        for i in range(rs,re+1):
            st=st+str(mat[i][ce])+" "
            count+=1
        ce-=1
        for i in range(ce,cs-1,-1):
            st=st+str(mat[re][i])+" "
            count+=1
        re-=1
        for i in range(re,rs-1,-1):
            st=st+str(mat[i][cs])+" "
            count+=1
        cs+=1

    print(st)



# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1