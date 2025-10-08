def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u + i)
    return temp
def fact(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f
n=int(input('enter no of data points'))
x=np.zeros((n))
y=np.zeros((n,n))
print("enter data for x and y:")
for i in range(n):
    x[i]=float(input('x['+str(i)+']='))
    y[i][0]=float(input('y['+str(i)+']='))
for i in range (1,n):
    for j in range (n-1,i-2,-1):
        y[j][i]=y[j][i-1]-y[j-1][i-1]
print('\n BACKWORD DIFFRENCE TABLE\n')
for i in range(0,n):
    print('%0.2f'%(x[i]),end='')
    for j in range(0,i+1):
         print('\t\t%0.2f'%(y[i][j]),end='')
    print()
value=float(input('Interpoluted value:'))
sum=y[n-1][0]
u=(value-x[n-1])/(x[1]-x[0])
for i in range(1,n):
    sum=sum+(u_cal(u,i)*y[n-1][i]/fact(i))
print("\n Interpoluted Value at",value,"is",sum)
