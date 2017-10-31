#encoding=utf-8    
#随机数，随机读取每一行的数据  
import linecache    
import random  

#oversampling
for i in range(0,6000,1):#for循环几次  
    a = random.randrange(1, 1128) #1-9中生成随机数  
    #print a  
    #从文件poem.txt中对读取第a行的数据  
    theline = linecache.getline(r'trainF', a)  
    print theline

'''
#undersampling
for i in range(0,10000,1):#for循环几次 
	a = random.randrange(1, 17550) #1-9中生成随机数     
	theline = linecache.getline(r'trainN', a)  
	print theline
'''