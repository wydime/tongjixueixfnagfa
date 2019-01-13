import  numpy as np


dataset=np.array([[3,3],[4,3],[1,1]])
flag   =np.array([1,1,-1])
def perceptron(dataset):
    w=np.array([0,0])
    b=0
    rate=1
    i=0
    time=0
    while i <3:
        c=flag[i]*( np.dot(w,dataset[i])+b)
        if c>0:
            print('此时数据集中的第'+str(i)+'个数数据正确判断')
            i=i+1

        else:
            print('此时数据集中的第' + str(i) + '错误判断判断')
            w=w+np.dot(flag[i],(dataset[i]))
            b=b+flag[i]
            i=0
            time = time + 1
        print(w,b)
        print(time)
    return
perceptron(dataset)