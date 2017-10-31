from numpy import loadtxt
y_hat = loadtxt('result0.03.csv', delimiter=",")
y = loadtxt('y.csv', delimiter=",")


list_time=[]
list_p=[]
list_starttime=[]
list_endtime=[]
list_faulttime=[]
list_truetime=[]
list_result=[]
for m in range(10,11,1):
	#m=float(t1)/10
	m=10.5	
	print m				
	print 'all fault timestamp:'	
    	for a1 in range(0,y_hat.size):
		if y_hat[a1]>m:
			xuhao=a1*20+1
			list_time.append(xuhao)
			list_p.append(y_hat[a1])	
			#print y_hat[i]
	#print list_time
	#print '--------------------------------'
	w=0
	list_starttime.append(list_time[0]+89999)
	while w<len(list_time)-1:
		chazhi=list_time[w+1]-list_time[w]
		if chazhi>106:
			list_endtime.append(list_time[w]+106+89999)
			list_starttime.append(list_time[w+1]+89999)
		w=w+1
	list_endtime.append(list_time[len(list_time)-1]+89999)

						

	for a111 in range(0,len(list_starttime)):
		print list_starttime[a111],
		print list_endtime[a111],
		print list_endtime[a111]-list_starttime[a111]
	print '----------------------'




        for a3 in range(90000,150000,1):
		for a4 in range(0,len(list_starttime)):
			if a3>=list_starttime[a4]  and a3<=list_endtime[a4]:
				list_faulttime.append(a3)

	for aa3 in range(90000,150000,1):
		if aa3 in list_faulttime:
			list_result.append('1')
		else:
			list_result.append('0')



	#for a33 in range(0,len(list_result)):
		#print list_result[a33]

	print '--------------------'



	print 'm='+str(m)
	FN=0
	FP=0
	print y[3]
	for a7 in range(0,len(y)):
		if y[a7]=='0' :
			FN=FN+1





	print 'FN='+str(FN)
	print 'FP='+str(FP)


	Nnormal=52564
	Nfault=3423
	he=Nnormal+Nfault
	#aa=float(Nfault)/float(he)
	#bb=float(Nnormal)/float(he)
	#haha1=float(FN)/Nnormal
	#haha2=float(FP)/Nfault
	#Score_1=(1-0.5*haha1-0.5*haha2)*100
	#Score_2=(1-aa*haha1-bb*haha2)*100
	#Score_3=(1-bb*haha1-aa*haha2)*100
						#print Score_1
	#print Score_2
						#print Score_3
	print '-------------------------------'
