def shell_sort(ary):
    n = len(ary)
    gap = round(n/2)       #初始步长 , 用round四舍五入取整
    while gap > 0 :
        print(gap)
        for i in range(gap,n):        #每一列进行插入排序 , 从gap 到 n-1
            temp = ary[i]
            j = i
            while ( j >= gap and ary[j-gap] > temp ):    #插入排序
                ary[j] = ary[j-gap]
                j = j - gap
            ary[j] = temp
        gap = round(gap/2)                     #重新设置步长
    return ary

def show(ary):
    print('Result is:',)
    for i in ary:
        print (i,end=' ')

if __name__ == '__main__':

    datas = [10, 1, 18, 30, 23, 12, 7, 5, 18, 17]
    bls = shell_sort(datas)
    show(bls)