import numpy as np
import scipy as sp
#最小二乘拟合
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
#目标函数
def real_fun(x):
    return np.sin(2*np.pi*x)
#计算多项式的值
def fit_func(p,x):
    f=np.poly1d(p)
    return f(x)
#计算残差
def residuals_func(p,x,y):
    ret=fit_func(p,x)-y
    return ret

x=np.linspace(0,1,10)
x_points=np.linspace(0,1,1000)
y_=real_fun(x)
y=[np.random.normal(0,0.1)+y1 for y1 in y_]
def fitting(M=0):
#M:为多项式的次数
    p_init=np.random.random(M+1)#随机生成M+1个数
##最小二乘法
    p_lsq=leastsq(residuals_func,p_init,args=(x,y))
    print('Fitting Parameters: ',p_lsq[0])
#可视化
    plt.plot(x_points,real_fun(x_points),label='real')
    plt.plot(x_points,fit_func(p_lsq[0],x_points),label='fitted curve')
    plt.plot(x, y, 'bo', label='noise')
    plt.legend()
    plt.show()
    return p_lsq
# M=0
p_lsq_0 = fitting(M=8)

