csvfile = open('F.csv', 'r')


for line in csvfile:
   	arr =  line.split(',')
	m='1';
	for a in range(0,len(arr)):
		m=m+' '+str(a+1)+':'+arr[a]
	print m,


