# -*- coding:utf8 -*-

class BubbleSort(object):

    def __init__(self, datas):
        self.datas = datas
        self.datas_len = len(datas)

    def sort(self):
        for i in range(self.datas_len-1):
            for j in range(self.datas_len-1-i):
                if(self.datas[j] > self.datas[j + 1]):
                    self.datas[j], self.datas[j+1] = self.datas[j+1], self.datas[j]

    def show(self):
        print('Result is:',)
        for i in self.datas:
            print (i,end=' ')

    #优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。
    #用一个标记记录这个状态即可。
    def sort2(self):
        for i in range(self.datas_len - 1):
            flag = 1  # 标记
            for j in range(self.datas_len - 1 - i):
                if (self.datas[j] > self.datas[j + 1]):
                    self.datas[j], self.datas[j + 1] = self.datas[j + 1], self.datas[j]
                    flag = 0
            if flag:  # 全排好序了，直接跳出
                break

if __name__ == '__main__':

    datas = [10, 1, 18, 30, 23, 12, 7, 5, 18, 17]
    bls = BubbleSort(datas)
    bls.sort2()
    bls.show()
