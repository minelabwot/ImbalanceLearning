# -*- encoding:utf-8 -*-  
#xgboost安装教程 参考 http://blog.csdn.net/lht_okk/article/details/54311333  
#xgboost原理参考 http://www.cnblogs.com/mfryf/p/6238185.html  
#http://blog.csdn.net/bryan__/article/details/52056112  
#xgboost 调参经验 http://blog.csdn.net/u010414589/article/details/51153310  
  
import xgboost as xgb  
import numpy as np  
  
#1,xgBoost的基本使用  
#2,自定义损失函数的梯度和二阶导  
#3,binary:logistic/logitraw  
  
# 定义f：theta*x  
  
#xgboost安装教程 参考 http://blog.csdn.net/lht_okk/article/details/54311333  
  
def log_reg(y_hat, y):  
    p = 1.0 / (1.0 + np.exp(-y_hat))  
    g = p - y.get_label()  
    h = p * (1.0-p)  
    return g, h  
  
  
def error_rate(y_hat, y):  
    return 'error', float(sum(y.get_label() != (y_hat > 0.5))) / len(y_hat)  
  
if __name__=="__main__":  
    #读取数据  
    data_train=xgb.DMatrix('train') 
    data_test=xgb.DMatrix('test_score')  
  
    #print 'data_train'  
    #print data_train  
    #print 'type(data_train)'  
    #print type(data_train)  
  
    #设置参数  
    #max_depth:树的最大深度,缺省值为6通常取值3-10  
  
    #eta:为了防止过拟合,更新过程中用到的收缩步长,在每次提升计算之后,算法会直接获得新特征的权重  
    #eta通过缩减特征的权重使得提升计算过程更加保守,默认值0.3  取值范围[0,1] 通常设置为[0.01-0.2]  
  
    #silent:取0时表示打印出运行时信息，取1时表示以缄默方式运行，不打印运行时信息。缺省值为0  
    #建议取0，过程中的输出数据有助于理解模型以及调参。另外实际上我设置其为1也通常无法缄默运行  
  
    #objective:缺省值 reg:linear 定义学习任务及相应的学习目标，可选目标函数如下：  
    # “reg:linear” –线性回归。  
    #“reg:logistic” –逻辑回归。  
    #“binary:logistic” –二分类的逻辑回归问题，输出为概率。  
    #“binary:logitraw” –二分类的逻辑回归问题，输出的结果为wTx。  
    #“count:poisson” –计数问题的poisson回归，输出结果为poisson分布,在poisson回归中，max_delta_step的缺省值为0  
    #“multi:softmax” –让XGBoost采用softmax目标函数处理多分类问题，同????貌??num_class（类?鸶鍪? 
    #“multi:softprob” –和softmax一样，但是输出的是ndata * nclass的向量，可以将该向量reshape成ndata行nclass列的矩阵。没行数据表示样本所属于每个类别的概率。  
    #“rank:pairwise” –set XGBoost to do ranking task by minimizing the pairwise loss  

    for ia in range(2,3,1):
    	for iia in range(3,4,1):
    		iia=float(iia)/100
    		for iii in range(10,11,1):
    			iii=float(iii)/10
    			for iiii in range(1,2,1):
    				for iiiii in range(70,80,10):
    					param={'silent':0,'max_depth':ia,'eta':0.3,'scale_pos_weight':iiii,'min_child_weight':0.5,'subsample':1,'booster':'gbtree','colsample_bytree':1,'objective':'binary:logistic'}  
					#param={'booster':'gbtree','objective':'binary:logistic'}  


	#param={'max_depth':6,'eta':0.01,'gamma':0.1,'min_child_weight': 0.01,'silent':1,'objective':'binary:logistic'}  
    					watchlist=[(data_test,'eval'),(data_train,'train')]  
    					n_round=iiiii
    #xgboost 基本方法和默认参数  
    #函数原型:xgboost.train(params,dtrain,num_boost_round=10,evals=(),obj=None,feval=None,maximize=False,early_stopping_rounds=None,evals_result=None,verbose_eval=True,learning_rates=None,xgb_model=None)  
    # params  
    # 这是一个字典，里面包含着训练中的参数关键字和对应的值，形式是params = {‘booster’:’gbtree’, ’eta’:0.1}  
    # dtrain  
    # 训练的数据  
    # num_boost_round  
    # 这是指提升迭代的个数  
    # evals  
    # 这是一个列表，用于对训练过程中进行评估列表中的元素。形式是evals = [(dtrain,’train’), (dval,’val’)]或者是evals = [  
    #     (dtrain,’train’)], 对于第一种情况，它使得我们可以在训练过程中观察验证集的效果。  
    # obj, 自定义目的函数  
    # feval, 自定义评估函数  
    # maximize, 是否对评估函数进行最大化  
    # early_stopping_rounds, 早期停止次数 ，假设为100，验证集的误差迭代到一定程度在100次内不能再继续降低，就停止迭代。这要求evals  
    # 里至少有  
    # 一个元素，如果有多个，按最后一个去执行。返回的是最后的迭代次数（不是最好的）。如果early_stopping_rounds  
    # 存在??蚰?型???鍪粜裕?bst.best_score, bst.best_iteration, 和bst.best_ntree_limit  
    # evals_result  
    # 字典，存储在watchlist  
    # 中的元素的评估结果。  
    # verbose_eval(可以输入布尔型或数值型)，也要求evals  
    # 里至少有  
    # 一个元素。如果为True, 则对evals中元素的评估结果会输出在结果中；如果输入数字，假设为5，则每隔5个迭代输出一次。  
    # learning_rates  
    # ?恳淮??升的学习率的列表? 
    # xgb_model, 在训练之前用于加载的xgb  
    # model。  
    					bst=xgb.train(param,data_train,num_boost_round=n_round,evals=watchlist,obj=log_reg,feval=error_rate)  
  					print param
  					print n_round
    #计算错误率  
					y_hat=bst.predict(data_test)
					y=data_test.get_label()  
    #print 'y_hat'   
    #print 'y'  
    #print y  

					list_time=[]
					list_p=[]
					list_starttime=[]
					list_endtime=[]
					list_faulttime=[]
					list_truetime=[]
    					for t1 in range(2,3,1):
						#m=float(t1)/10
						m=0.000000000000001					
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


				


						for a2 in range(0,len(list_starttime)):
							if list_endtime[a2]-list_starttime[a2]<106:
								del list_endtime[a2]
								del list_starttime[a2]
						

						for a111 in range(0,len(list_starttime)):
							print list_starttime[a111],
							print list_endtime[a111],
							print list_endtime[a111]-list_starttime[a111]
						print '----------------------'



						for a3 in range(0,200000):
							for a4 in range(0,len(list_starttime)):
								if a3>=list_starttime[a4]  and a3<=list_endtime[a4]:
									list_faulttime.append(a3)
	#print list_faulttime

						start_true=[91127,141194,143056,144947,147370,148543]
						end_true=[91343,141627,143469,145897,148320,148998]



						for a5 in range(0,200000):
							for a6 in range(0,len(start_true)):
								if a5>=start_true[a6] and a5<=end_true[a6]:
									list_truetime.append(a5)
	
	#print list_truetime
						print m
						zhengque_sum0=0
						zhengque_sum1=0	
						for a7 in range(0,len(list_faulttime)):
							if list_faulttime[a7] in list_truetime:
								zhengque_sum0=zhengque_sum0+1
						FN=len(list_faulttime)-zhengque_sum0
						print FN

						for a8 in range(0,len(list_truetime)):
							if list_truetime[a8] in list_faulttime:
								zhengque_sum1=zhengque_sum1+1
						FP=len(list_truetime)-zhengque_sum1
						print FP


						Nnormal=52564
						Nfault=3423
						he=Nnormal+Nfault
						aa=float(Nfault)/float(he)
						bb=float(Nnormal)/float(he)
						haha1=float(FN)/Nnormal
						haha2=float(FP)/Nfault
						Score_1=(1-0.5*haha1-0.5*haha2)*100
						Score_2=(1-aa*haha1-bb*haha2)*100
						Score_3=(1-bb*haha1-aa*haha2)*100
						print Score_1
						print Score_2
						print Score_3
						print '-------------------------------'
		
		






'''

k=10
while k<100:
	m=float(k)/100
	k=k+10
	print m
	sum1=0
	sum0=0
	error=sum(y!=(y_hat>m))   
	error_rate=float(error)/len(y_hat) 


	print 'sample_sum  =\t',len(y_hat)  
	print 'error_num1  =\t%4d'%error
	print 'error_rate  =\t%.5f%%'%(100*error_rate)

	#将故障预测为正常，故障没有识别的概率。
	for i in range(0,y_hat.size):
		if y[i]==1:
			if y_hat[i]<m:
				sum1=sum1+1
	print 'sum1_error:'+str(sum1)
	print 'sum1:'+str(sum(y==1))
	error_sum1=float(sum1)/sum(y==1)
	print 'error:'+str(error_sum1)

	#将正常预测为故障，错误的识别故障的概率。
	for i in range(0,y_hat.size):
		if y[i]==0:
			if y_hat[i]>=m:
				sum0=sum0+1
	print 'sum0_error:'+str(sum0)
	print 'sum0:'+str(sum(y==0))
	error_sum0=float(sum0)/sum(y==0)
	print 'error:'+str(error_sum0)


	sum2=sum(y==2)
	#print sum2

	S=(1-0.5*error_sum0-0.5*error_sum1)*100
	print S
	print '---------------------------------------------------'

'''













'''
m=0.001
sum1=0
sum0=0
error=sum(y!=(y_hat>m))   
error_rate=float(error)/len(y_hat) 


print 'sample_sum  =\t',len(y_hat)  
print 'error_num1  =\t%4d'%error
print 'error_rate  =\t%.5f%%'%(100*error_rate)

#将故障预测为正常，故障没有识别的概率。
for i in range(0,y_hat.size):
	if y[i]==1:
		if y_hat[i]<m:
			sum1=sum1+1
print 'sum1_error:'+str(sum1)
print 'sum1:'+str(sum(y==1))
error_sum1=float(sum1)/sum(y==1)
print 'error:'+str(error_sum1)

#将正常预测为故障，错误的识别故障的概率。
for i in range(0,y_hat.size):
	if y[i]==0:
		if y_hat[i]>=m:
			sum0=sum0+1
print 'sum0_error:'+str(sum0)
print 'sum0:'+str(sum(y==0))
error_sum0=float(sum0)/sum(y==0)
print 'error:'+str(error_sum0)


sum2=sum(y==2)
#print sum2

S=(1-0.5*error_sum0-0.5*error_sum1)*100
print S
'''

'''
for i in range(0,y_hat.size):
	print y_hat[i]
'''


'''
for i in range(0,y_hat.size):
	if y_hat[i]>0.4:
		print '1'
	if y_hat[i]<=0.4:
		print '0'

print 'haha'
for i in range(0,y.size):
	print y[i]
'''