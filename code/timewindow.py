from compiler.ast import flatten
from numpy import loadtxt

dataset = loadtxt('21_test.csv', delimiter=",")

buchang = 10
shijianchuang = 80



def getFeature(juzhen):
	for i in range(0,len(juzhen),buchang):
		if i+shijianchuang<len(juzhen):
			M = juzhen[i:i+shijianchuang,0:]
			m = M.tolist()
			MM = flatten(m)
			MMM = str(MM)
			MMMM=MMM[1:len(MMM)-1]
			print MMMM



'''
M1=dataset[90000:150000,0:26]
getFeature(M1)

'''



'''
#failure
M1 = dataset[12290:12949,0:26]
M2 = dataset[54032:54779,0:26]
M3 = dataset[58216:59167,0:26]
M4 = dataset[80459:81410,0:26]
M5 = dataset[91126:91343,0:26]
M6 = dataset[141193:141627,0:26]
M7 = dataset[143055:143469,0:26]
M8 = dataset[144946:145897,0:26]
M9 = dataset[147369:148320,0:26]
M10 = dataset[148542:148998,0:26]
#M5 = dataset[91126:91343,0:26]
#M6 = dataset[141193:141627,0:26]
#M7 = dataset[143055:143469,0:26]
#M8 = dataset[144946:145897,0:26]
#M9 = dataset[147369:148320,0:26]
#M10 = dataset[148542:148998,0:26]
M11 = dataset[167019:167970,0:26]
M12 = dataset[176278:177229,0:26]
M13 = dataset[179744:180798,0:26]
M14 = dataset[183272:184223,0:26]
'''



#21_test.csv
#21normal
M1 = dataset[0:12020,0:26]
M2 = dataset[12949:53032,0:26]
M3 = dataset[54779:57216,0:26]
M4 = dataset[59167:79884,0:26]
M5 = dataset[81410:90000,0:26]
#M5 = dataset[81410:91126,0:26]
#M6 = dataset[91343:140193,0:26]
#M7 = dataset[141627:142264,0:26]
#M8 = dataset[143469:143946,0:26]
#M9 = dataset[145897:146369,0:26]
#M10 = dataset[148998:166019,0:26]
M6 = dataset[91343:140193,0:26]
M7 = dataset[141627:142264,0:26]
M8 = dataset[143469:143946,0:26]
M9 = dataset[145897:146369,0:26]
M10 = dataset[150000:166019,0:26]
M11 = dataset[167970:175278,0:26]
M12 = dataset[177229:178676,0:26]
M13 = dataset[180798:182272,0:26]
M14 = dataset[184223:190494,0:26]


getFeature(M1)
getFeature(M2)
getFeature(M3)
getFeature(M4)
getFeature(M5)
getFeature(M6)
getFeature(M7)
getFeature(M8)
getFeature(M9)
getFeature(M10)
#getFeature(M5)
#getFeature(M6)
#getFeature(M7)
#getFeature(M8)
#getFeature(M9)
#getFeature(M10)
getFeature(M11)
getFeature(M12)
getFeature(M13)
getFeature(M14)


'''
M1=dataset[:,0:26]
getFeature(M1)
'''

'''
M1 = dataset[0:443,0:26]
M2 = dataset[443:708,0:26]
M3 = dataset[708:1659,0:26]
M4 = dataset[1659:2809,0:26]
M5 = dataset[2809:3760,0:26]
M6 = dataset[3760:3866,0:26]
M7 = dataset[3866:4218,0:26]
M8 = dataset[4218:5170,0:26]
M9 = dataset[5170:6121,0:26]
M10 = dataset[6121:7408,0:26]
M11 = dataset[7408:8360,0:26]
M12 = dataset[8360:9614,0:26]
M13 = dataset[9614:9761,0:26]
M14 = dataset[9761:10712,0:26]
M15 = dataset[10712:11328,0:26]
M16 = dataset[11328:12278,0:26]
M17 = dataset[12278:13229,0:26]
M18 = dataset[13229:14026,0:26]
M19 = dataset[14026:14977,0:26]
M20 = dataset[14977:15928,0:26]
M21 = dataset[15928:17171,0:26]
M22 = dataset[17171:18081,0:26]
M23 = dataset[18081:18626,0:26]
M24 = dataset[18626:19577,0:26]
M25 = dataset[19577:20169,0:26]
M26 = dataset[20169:21039,0:26]
M27 = dataset[21039:21991,0:26]
M28 = dataset[21991:22942,0:26]
M29 = dataset[22942:23894,0:26]




getFeature(M1)
getFeature(M2)
getFeature(M3)
getFeature(M4)
getFeature(M5)
getFeature(M6)
getFeature(M7)
getFeature(M8)
getFeature(M9)
getFeature(M10)
getFeature(M11)
getFeature(M12)
getFeature(M13)
getFeature(M14)
getFeature(M15)
getFeature(M16)
getFeature(M17)
getFeature(M18)
getFeature(M19)
getFeature(M20)
getFeature(M21)
getFeature(M22)
getFeature(M23)
getFeature(M24)
getFeature(M25)
getFeature(M26)
getFeature(M27)
getFeature(M28)
getFeature(M29)
'''


'''
M1 = dataset[0:4755,0:26]
M2 = dataset[4755:5725,0:26]
M3 = dataset[5725:48746,0:26]
M4 = dataset[48746:52130,0:26]
M5 = dataset[52130:91616,0:26]
M6 = dataset[91616:126649,0:26]
M7 = dataset[126649:140666,0:26]
M8 = dataset[140666:142786,0:26]
M9 = dataset[142786:172336,0:26]
M10 = dataset[172336:173658,0:26]
M11 = dataset[173658:176869,0:26]
M12 = dataset[176869:190123,0:26]
M13 = dataset[190123:196636,0:26]
M14 = dataset[196636:197317,0:26]
M15 = dataset[197317:209366,0:26]
M16 = dataset[209366:212333,0:26]
M17 = dataset[212333:231459,0:26]
M18 = dataset[231459:232021,0:26]
M19 = dataset[232021:232152,0:26]
M20 = dataset[232152:234740,0:26]
M21 = dataset[234740:250190,0:26]
M22 = dataset[250190:268867,0:26]
M23 = dataset[268867:273893,0:26]
M24 = dataset[273893:293945,0:26]
M25 = dataset[293945:302529,0:26]
M26 = dataset[302529:350257,0:26]



getFeature(M1)
getFeature(M2)
getFeature(M3)
getFeature(M4)
getFeature(M5)
getFeature(M6)
getFeature(M7)
getFeature(M8)
getFeature(M9)
getFeature(M10)
getFeature(M11)
getFeature(M12)
getFeature(M13)
getFeature(M14)
getFeature(M15)
getFeature(M16)
getFeature(M17)
getFeature(M18)
getFeature(M19)
getFeature(M20)
getFeature(M21)
getFeature(M22)
getFeature(M23)
getFeature(M24)
getFeature(M25)
getFeature(M26)
'''
