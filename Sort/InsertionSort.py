

class InsertSort(object):

    def __init__(self, datas):
        self.datas = datas
        self.datas_len = len(datas)

    def sort(self):
        for i in range(1,self.datas_len):
            temp=self.datas[i]
            flag=i
            for j in range(i-1, -1, -1):
                if(temp < self.datas[j]):
                    self.datas[j+1] = self.datas[j]
                    flag=j
            self.datas[flag]=temp


    def show(self):
        print('Result is:',)
        for i in self.datas:
            print (i,end=' ')


if __name__ == '__main__':

    datas = [10, 1, 18, 30, 23, 12, 7, 5, 18, 17]
    bls = InsertSort(datas)
    bls.sort()
    bls.show()