#马青公式：π/4 = 4x(1/(1x5)-1/(3x5^3)+1/(5x5^5)-1/(7x5^7)+...)-(1/(1x239)-1/(3x239^3)+1/(5x5^3)-1/(7x5^7)+...)
#计算n位就在上述公式两边乘以10^n，那么左边是整数，右边每项也取整数即可

n = int(input('请键入想要计算到小数点后的位数:'))        
t = n+10                                            # 多计算10位，防止尾数取舍的影响
b = 10**t                                           # 为算到小数点后t位，两边乘以10^t
x1 = b*4//5                                         # 取整求含4/5的首项
x2 = b // -239                                      # 取整求含1/239的首项
s = x1+x2                                           # 求第一大项
n *= 2                                              # 设置下面循环的终点，即共计算n项
for i in range(3, n, 2):                            # 循环初值=3，末值n,步长=2
    x1 //= -25                                      # 取整求每个含1/5的项及符号
    x2 //= -57121                                   # 取整求每个含1/239的项及符号
    x = (x1+x2) // i                                # 求两项之和，除以对应因子，取整
    s += x                                          # 求总和
pai = s*4                                           # 求出π
pai //= 10**10                                      # 舍掉后十位
print(pai)                                          # 输出圆周率π的值，不带小数点
