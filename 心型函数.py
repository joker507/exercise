#心型函数y = (x**(2/3) + sqrt(x**(4/3) - 4*x**2+4)/2
#       y = (x**(2/3) - sqrt(x**(4/3) - 4*x**2+4)/2

'''
心形线的数学表达式

极坐标方程
水平方向： r=a(1-cosθ) 或 r=a(1+cosθ) (a>0)
垂直方向： r=a(1-sinθ) 或 r=a(1+sinθ) (a>0)
直角坐标方程
心形线的平面直角坐标系方程表达式分别为 x^2+y^2+a*x=a*sqrt(x^2+y^2) 和 x^2+y^2-a*x=a*sqrt(x^2+y^2）
参数方程
x=a*(2*cos(t)-cos(2*t))
y=a*(2*sin(t)-sin(2*t))
所围面积为3/2*PI*a^2，形成的弧长为8a
————————————————
版权声明：本文为CSDN博主「MyHuster」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/thao6626/article/details/46639749
'''

__author__ = 'taohao'

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math

def drawHeart_byprint():
    print('\n'.join([''.join([('lovezhi.'[(x - y) % 8] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
                x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))

def drawHeart():
    t = np.linspace(0, math.pi, 1000)
    x = np.sin(t)
    y = np.cos(t) + np.power(x, 2.0 / 5)
    plt.plot(x, y, color='red', linewidth=2, label='h')
    plt.plot(-x, y, color='red', linewidth=2, label='-h')
    plt.xlabel('t')
    plt.ylabel('h')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

    plt.legend()
    plt.show()

drawHeart()



