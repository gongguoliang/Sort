def merge_sort(ary):
    if len(ary) <= 1 : return ary
    num = int(len(ary)/2)       #二分分解
    left = merge_sort(ary[:num])
    right = merge_sort(ary[num:])
    return merge(left,right)    #合并数组

def merge(left,right):
    l,r = 0,0           #left与right数组的下标指针
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

def show(ary):
    print('Result is:',)
    for i in ary:
        print (i,end=' ')

if __name__ == '__main__':

    datas = [10, 1, 18, 30, 23, 12, 7, 5, 18, 17]
    bls = merge_sort(datas)
    show(bls)