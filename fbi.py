def fibo(n):
	if(n==1 or n==2) :
		return 1
	else :
		return fibo(n-1) + fibo(n-2)
def fibo21(n):
	a= 1
	b= 1
	for i in range (3, n+1) :
		tmp = a
		a= a + b
		b= tmp
	return a
n = input( 'give me something\n' )
import time 
start = time.time()
print fibo21(n)
end = time.time()
print 'time' , end-start

