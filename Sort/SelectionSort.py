# -*- coding:utf8 -*-

def select_sort(ary):
    n = len(ary)
    for i in range(0, n):
        min = i  # 最小元素下标标记
        for j in range(i + 1, n):
            if ary[j] < ary[min]:
                min = j  # 找到最小值的下标
        ary[min], ary[i] = ary[i], ary[min]  # 交换两者
    return ary

def show(ary):
        print('Result is:',)
        for i in ary:
            print (i,end=' ')

if __name__ == '__main__':

    datas = [10, 1, 18, 30, 23, 12, 7, 5, 18, 17]
    bls = select_sort(datas)
    show(bls)