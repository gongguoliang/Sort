def quick_sort(ary):
    return qsort(ary,0,len(ary)-1)

def qsort(ary,left,right):

    if left >= right :
        return ary

    key = ary[left]     #取最左边的为基准数
    lp = left           #左指针
    rp = right          #右指针
    while lp < rp :
        while ary[rp] >= key and lp < rp :
            rp -= 1
        while ary[lp] <= key and lp < rp :
            lp += 1
        ary[lp],ary[rp] = ary[rp],ary[lp]

    ary[left],ary[lp] = ary[lp],ary[left]
    qsort(ary,left,lp-1)
    qsort(ary,rp+1,right)
    return ary

def show(ary):
    print('Result is:', )
    for i in ary:
        print(i, end=' ')

if __name__ == '__main__':

    datas = [10, 1, 18, 30, 23, 12, 7, 5, 18, 17]
    bls = quick_sort(datas)
    show(bls)