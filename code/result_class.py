from numpy import loadtxt
y_hat = loadtxt('result_class.csv', delimiter=",")
y=loadtxt('test_y', delimiter=",")



for m in range(20,50,1):
	#m=10.5
	m=float(m)/10
	print m


	sum1=0
	sum0=0
	error=sum(y!=(y_hat>m))   
	error_rate=float(error)/len(y_hat) 


	print 'sample_sum  =\t',len(y_hat)  
	print 'error_num1  =\t%4d'%error
	print 'error_rate  =\t%.5f%%'%(100*error_rate)


	for i in range(0,y_hat.size):
		if y[i]==1:
			if y_hat[i]<m:
				sum1=sum1+1
	print 'sum1_error:'+str(sum1)
	print 'sum1:'+str(sum(y==1))
	error_sum1=1-(float(sum1)/sum(y==1))
	print 'zhengque:'+str(error_sum1)


	for i in range(0,y_hat.size):
		if y[i]==0:
			if y_hat[i]>=m:
				sum0=sum0+1
	print 'sum0_error:'+str(sum0)
	print 'sum0:'+str(sum(y==0))
	error_sum0=1-(float(sum0)/sum(y==0))	
	print 'zhengque:'+str(error_sum0)
	print '-----------------------------------'

