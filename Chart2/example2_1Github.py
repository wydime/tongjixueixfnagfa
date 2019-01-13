import  pandas as pd
import  numpy  as np
from  sklearn.datasets import  load_iris
import  matplotlib.pyplot as plt
#load data
iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df['label']=iris.target
data=np.array(df.iloc[:100,[0,1,-1]])
X,y=data[:,:-1],data[:,-1]
y=np.array([1 if i==1 else -1 for i in y])
#
# df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'label']
# print(df.label.value_counts())
# plt.scatter(df[0:50]['sepal length'],df[0:50]['sepal width'],label='0')
# plt.scatter(df[50:100]['sepal length'],df[50:100]['sepal width'],label='1')
# plt.xlabel('sepal length')
# plt.xlabel('sepal width')
# plt.legend()
# plt.show()
class Model:
    def __init__(self):
        self.w=np.ones(len(data[0])-1,dtype=np.float32)
        self.b=0
        self.l_rate=0.1
    def sign(self,w,b,x):
        return np.dot(w,x)+b
    def fit(self,X_train,y_train):
        is_wrong=False
        while not is_wrong:
            wrong_count=0
            for d in range(len(X_train)):
                X=X_train[d]
                y=y_train[d]
                if y*self.sign(self.w,self.b,X)<=0:
                    self.w=self.w+np.dot(y,X)*self.l_rate
                    self.b=self.b+self.l_rate*y
                    wrong_count+=1
            if wrong_count==0:
                is_wrong=True
        return 'Perceptron Model!'
    def score(self):
        pass
percetron=Model()
percetron.fit(X,y)
x_points=np.linspace(4,7,10)
y_points=-(percetron.w[0]*x_points+percetron.b)/percetron.w[1]
plt.plot(x_points,y_points)

plt.plot(data[:50, 0], data[:50, 1], 'bo', color='blue', label='0')
plt.plot(data[50:100, 0], data[50:100, 1], 'bo', color='orange', label='1')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend()
plt.show()