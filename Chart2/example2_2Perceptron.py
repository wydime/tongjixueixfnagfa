import numpy as np
dataset=np.array([[3,3],[4,3],[1,1]])
flag   =np.array([1,1,-1])
def perceptron2():

    a=[0]*3
    b=0
    gram_mat = np.dot(dataset, dataset.T)
    #控制整体的循环次数'
    i=0
    while i<3:
        tem=[]
        for j in range(3):
            tem.append(a[j]*flag[j]*gram_mat[i,j])
        s1=sum(tem)
        conditon=flag[i]*(s1+b)
        if conditon<=0:
            a[i]+=1
            b+=flag[i]
            print('第'+str(i)+'数据误分类,')
            i=0
        else:
            # print('第'+str(i)+'数据正确分类')
            i+=1
        print(a,b)

    print()






perceptron2()




