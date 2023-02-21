if __name__ == '__main__':
    arr=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        li = [name, score]
        arr.append(li)
    high=1000000
    low=arr[0][1]
    for i in range(len(arr)):
        if low>arr[i][1]:
            temp=low
            low=arr[i][1]
            high=temp
        elif low<arr[i][1] and high>arr[i][1]:
            high=arr[i][1]
    new_list=[]
    for i in arr:
        if high==i[1]:
            new_list.append(i)
    new_list.sort()
    for i in new_list:
        print(i[0])