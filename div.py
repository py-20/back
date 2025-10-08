n=int(input('enter no of data points'))
x=np.zeros((n))
y=np.zeros((n,n))
print("enter data for x and y:")
for i in range(n):
    x[i]=float(input('x['+str(i)+']='))
    y[i][0]=float(input('y['+str(i)+']='))
for i in range (1,n):
    for j in range (0,n-i):
        y[j][i]=(y[j+1][i-1]-y[j][i-1])/(x[j+i]-x[j])
print('\n DIVIDED DIFFRENCE TABLE\n')
for i in range(0,n):
    print('%0.2f'%(x[i]),end='')
    for j in range(0,n-i):
         print('\t\t%0.2f'%(y[i][j]),end='')
    print()
value=float(input('value:'))
sum=y[0][0]
for i in range(1,n):
    sum=sum+((value-x[i])*y[0][i])
print("\n Interpoluted Value at",value,"is",round(sum,n))