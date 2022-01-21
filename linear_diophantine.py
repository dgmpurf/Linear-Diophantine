#Ke Ma
#11621365
from itertools import product
from collections import defaultdict
import itertools

choose = input("Function number input(1 or 2): ")

#input C1,C2,C3 to get Cmax

def part123(vC1,vC2,vC3,vC):
	"""
	Preparation 1
	"""
	make_edge = []
	#inital Cmax value
	cMaxValue = 0
	#if c1,c2,c3 all + or -
	if (int(vC1) >= 0 and int(vC2) >= 0 and int(vC3) >= 0) or (int(vC1) <= 0 and int(vC2) <= 0 and int(vC3) <= 0):
		cMaxValue = abs(int(vC1)) + abs(int(vC2)) + abs(int(vC3))
		#add b
		if (int(vC1) >= 0 and int(vC2) >= 0 and int(vC3) >= 0):
			cMaxValue = cMaxValue + 1
	#only c1 - c2,c3 + or c1 + c2,c3 -
	elif (int(vC1) <= 0 and int(vC2) >= 0 and int(vC3) >= 0) or (int(vC1) >= 0 and int(vC2) <= 0 and int(vC3) <= 0):
		if (abs(int(vC1)) - abs(int(vC2)) - abs(int(vC3))) > 0:
			cMaxValue = abs(int(vC1))
			#add b
			if int(vC1) >= 0:
				cMaxValue = cMaxValue + 1
		else:
			cMaxValue = abs(int(vC2)) + abs(int(vC3))
			#add b
			if (int(vC2) >= 0 and int(vC3) >= 0):
				cMaxValue = cMaxValue + 1
	#only c2 - c1,c3 + or c2 + c1,c3 -
	elif (int(vC1) >= 0 and int(vC2) <= 0 and int(vC3) >= 0) or (int(vC1) <= 0 and int(vC2) >= 0 and int(vC3) <= 0):
		if (abs(int(vC2)) - abs(int(vC1)) - abs(int(vC3))) > 0:
			cMaxValue = abs(int(vC2))
			#add b
			if int(vC2) >= 0:
				cMaxValue = cMaxValue + 1
		else:
			cMaxValue = abs(int(vC1)) + abs(int(vC3))
			#add b
			if (int(vC1) >= 0 and int(vC3) >= 0):
				cMaxValue = cMaxValue + 1
	#only c3 - c2,c3 + or c3 + c2,c3 -
	elif (int(vC1) >= 0 and int(vC2) >= 0 and int(vC3) <= 0) or (int(vC1) <= 0 and int(vC2) <= 0 and int(vC3) >= 0):
		if (abs(int(vC3)) - abs(int(vC1)) - abs(int(vC2))) > 0:
			cMaxValue = abs(int(vC2))
			#add b
			if int(vC3) >= 0:
				cMaxValue = cMaxValue + 1
		else:
			cMaxValue = abs(int(vC1)) + abs(int(vC2))
			#add b
			if (int(vC1) >= 0 and int(vC2) >= 0):
				cMaxValue = cMaxValue + 1
	else:
		False
	#print Cmax
	print("Cmax: " + str(cMaxValue))

	"""
	Preparation 2
	"""
	inputvalue = vC
	#value use bin conver to string binary
	inputstring = bin(int(inputvalue))
	#remove 0B
	fixedInputBinString = inputstring.replace('0b','')
	#print(fixedInputString)
	#length of string
	lengthofstring=len(fixedInputBinString)
	#make str to separete int list
	blist = [int(x) for x in fixedInputBinString]
	#i=Kc+1
	addedb = blist.append(0)
	#reverse blist
	revblist = blist[::-1]
	#save a dic for revblist
	bdic = {i:revblist[i] for i in range(0, len(revblist))}
	#print(bdic)
	#Kc length
	Kc = len(blist) - 1
	#print Kc value
	print('Kc:' + str(Kc))
	#print bi from dict
	bIndexnum = 1
	for value in bdic.values():
		print('b' + str(bIndexnum) + ' ' + str(value))
		bIndexnum += 1
	"""
	Alg1.
	"""
	#make edge
	for carry in range(-cMaxValue,cMaxValue+1):
		for im in range(1, Kc+2):
			for carrypr in range(-cMaxValue,cMaxValue+1):
				for ipr in range(1, Kc+2):
					for a1 in range(2):
						for a2 in range(2):
							for a3 in range(2):
								#get R
								R = int(vC1)*a1 + int(vC2)*a2 + int(vC3)*a3 + blist[im-1] + carry
								if R%2==0 and carrypr == R/2:
									# 1 <= i <= Kc
									if im in range(1,Kc+1) and ipr == im + 1:
										#store each edge in tuple
										edge_tuple = (carry,im,carrypr,ipr,a1,a2,a3)
										#append in list
										make_edge.append(edge_tuple)
									elif ipr == im:
										#store each edge in tuple
										edge_tuple = (carry,im,carrypr,ipr,a1,a2,a3)
										#append in list
										make_edge.append(edge_tuple)
	#print graph
	fix_edge = list(set(make_edge))
	count = len(fix_edge)
	Ksc = (Kc)
	print(fix_edge)
	print(count)
	#make it globle
	fix_edge.append(Ksc)
	return fix_edge

"""
Alg2.
"""
if int(choose) == 1:
	aa = input("Equation for Cmax, Equation C1x1 + C2x2 + C3x3 + C = 0, value C1: ")
	ss = input("value C2: ")
	dd = input("value C3: ")
	ff = input("value C: ")
	part123(aa,ss,dd,ff)

ll=[]
recodM1F = []
recodM2F = []
recodM1N = []
recodM2N = []
recodM1T = []
recodM2T = []
rlsl1=[]
rlsl2=[]
rlsl3=[]
rec1 = []
rec2 = []
finalsteplist = []
fix_list = []
x1=0
x2=0
x3=0
finalsteplist1 = []
finalsteplist2 = []
finalsteplist3 = []
finalsteplist = []
producta123 = []
producta123list = []
producta123list1 = []
ele14list = []
ele14llist = []
redele14list = []
initnotfixMnode = []
initMnode = []
acceptnotfix = []
accpMnode = []
tempfin = []
finlist = []

fix_edge1 = []
fix_edge2 = []
productnotfixa123 = []
makea123list = ()
tempfin1 = []
tempfin2 = []
tempfin3 = []
finlist1 = []
finalstepllist1 =[]
finalstepllist2 =[]
finalstepllist3 =[]

a = 3
b = -2
c = -1
d = 3

a1 = 6
b1 = -4
c1 = 1
d1 = 3

list1 =[]
list2 =[]
list3 =[]
list1a =[]
list2a =[]
list3a =[]
list1b =[]
list2b =[]
list3b =[]

if int(choose) == 2:
	print("Pre-set 3,-2,-1,3 as M1, 6,-4,1,3 as M2")
	# M1
	fix_edge1 = part123(a,b,c,d)
	#Kc1
	Kc1 = fix_edge1[-1]
	Ksc1 = int(Kc1)
	fix_edge1.pop()

	# M2
	fix_edge2 = part123(a1,b1,c1,d1)
	#Kc
	Kc2 = fix_edge2[-1]
	fix_edge2.pop()
	Ksc2 = int(Kc2)

	list0 = list(product(fix_edge1,fix_edge2))

	for a123 in range(0,len(list0)):
		makea123list = list0[a123]
		if makea123list[0][4] == makea123list[1][4] and makea123list[0][5] == makea123list[1][5] and makea123list[0][6] == makea123list[1][6]:
    			productnotfixa123.append(list0[a123])
	producta123 = productnotfixa123
	producta123list = list(itertools.chain(*producta123))
	producta123list1 = list(itertools.chain(*producta123list))
	ele14list=list(zip(*[iter(producta123list1)]*14))


	for i in range(0,len(ele14list)):
		#initTempleMnode = ele14list[i]
		if ele14list[i][0] == 0 and ele14list[i][1] == 1 and ele14list[i][7] == 0 and ele14list[i][8] == 1:
			initnotfixMnode.append(ele14list[i])
	initMnode = initnotfixMnode
	#print(initMnode)

	for j in range(0,len(ele14list)):
		if ele14list[j][2] == 0 and ele14list[j][3] == Ksc1+1 and ele14list[j][9] == 0 and ele14list[j][10] == Ksc2+1:
			acceptnotfix.append(ele14list[j])
	accpMnode = acceptnotfix
	#print(accpMnode)

	for m in range(0,len(initMnode)):
		for n in range(0,len(accpMnode)):
			if initMnode[m][2] == accpMnode[n][0] and initMnode[m][3] == accpMnode[n][1] and initMnode[m][9] == accpMnode[n][7] and initMnode[m][10] == accpMnode[n][8]:
				tempfin.append(initMnode[m])
				tempfin.append(accpMnode[n])
				#print(tempfin)
	finlist = tempfin
	#print(tempfin)

	fset = set(ele14list)-set(initMnode)
	fset1 = set(fset) - set(accpMnode)
	fli = list(fset)
	#print(fli)

	for m in range(0,len(initMnode)):
		for n in range(0,len(fli)):
			for p in range(0,len(accpMnode)):
				if initMnode[m][2] == fli[n][0] and initMnode[m][3] == fli[n][1] and initMnode[m][9] == fli[n][7] and initMnode[m][10] == fli[n][8] and fli[n][2] == accpMnode[p][0] and fli[n][3] == accpMnode[p][1] and fli[n][9] == accpMnode[p][7] and fli[n][10] == accpMnode[p][8]:
						tempfin1.append(initMnode[m])
						tempfin2.append(fli[n])
						tempfin3.append(accpMnode[p])
	#reduce repeated
	#reduce_list = list(set([i for i in list5]))
	for i in range(len(tempfin1)):
		finalsteplist1.append(tempfin1[i][11:])
	finalstepllist1 = finalsteplist1

	for i in range(len(tempfin2)):
		finalsteplist2.append(tempfin2[i][11:])
	finalstepllist2 = finalsteplist2

	for i in range(len(tempfin3)):
		finalsteplist3.append(tempfin3[i][11:])
	finalstepllist3 = finalsteplist3
	print(finalstepllist1)
	print(finalstepllist2)
	print(finalstepllist3)

	tuple1 = (finalstepllist1[0][0],) + (finalstepllist2[0][0],) + (finalstepllist3[0][0],)
	tuple2 = (finalstepllist1[0][1],) + (finalstepllist2[0][1],) + (finalstepllist3[0][1],)
	tuple3 = (finalstepllist1[0][2],) + (finalstepllist2[0][2],) + (finalstepllist3[0][2],)

	list1 = list(tuple1)
	list2 = list(tuple2)
	list3 = list(tuple3)
	list1.reverse()
	list2.reverse()
	list3.reverse()

	ansstr1 = [str(list1) for list1 in list1]
	ansstr2 = [str(list2) for list2 in list2]
	ansstr3 = [str(list3) for list3 in list3]
	anss1 = "".join(ansstr1)
	anss2 = "".join(ansstr2)
	anss3 = "".join(ansstr3)
	x1 = int(anss1,2)
	x2 = int(anss2,2)
	x3 = int(anss3,2)
	print("First")
	print("x1 = " + str(x1))
	print("x2 = " + str(x2))
	print("x3 = " + str(x3))

	tuple1a = (finalstepllist1[1][0],) + (finalstepllist2[1][0],) + (finalstepllist3[1][0],)
	tuple2a = (finalstepllist1[1][1],) + (finalstepllist2[1][1],) + (finalstepllist3[1][1],)
	tuple3a = (finalstepllist1[1][2],) + (finalstepllist2[1][2],) + (finalstepllist3[1][2],)

	list1a = list(tuple1a)
	list2a = list(tuple2a)
	list3a = list(tuple3a)
	list1a.reverse()
	list2a.reverse()
	list3a.reverse()

	ansstr1a = [str(list1a) for list1a in list1a]
	ansstr2a = [str(list2a) for list2a in list2a]
	ansstr3a = [str(list3a) for list3a in list3a]
	anss1a = "".join(ansstr1a)
	anss2a = "".join(ansstr2a)
	anss3a = "".join(ansstr3a)
	x1a = int(anss1a,2)
	x2a = int(anss2a,2)
	x3a = int(anss3a,2)
	print("Second")
	print("x1 = " + str(x1a))
	print("x2 = " + str(x2a))
	print("x3 = " + str(x3a))

	tuple1b = (finalstepllist1[2][0],) + (finalstepllist2[2][0],) + (finalstepllist3[2][0],)
	tuple2b = (finalstepllist1[2][1],) + (finalstepllist2[2][1],) + (finalstepllist3[2][1],)
	tuple3b = (finalstepllist1[2][2],) + (finalstepllist2[2][2],) + (finalstepllist3[2][2],)

	list1b = list(tuple1b)
	list2b = list(tuple2b)
	list3b = list(tuple3b)
	list1b.reverse()
	list2b.reverse()
	list3b.reverse()

	ansstr1b = [str(list1b) for list1b in list1b]
	ansstr2b = [str(list2b) for list2b in list2b]
	ansstr3b = [str(list3b) for list3b in list3b]
	anss1b = "".join(ansstr1b)
	anss2b = "".join(ansstr2b)
	anss3b = "".join(ansstr3b)
	x1b = int(anss1b,2)
	x2b = int(anss2b,2)
	x3b = int(anss3b,2)
	print("Third")
	print("x1 = " + str(x1b))
	print("x2 = " + str(x2b))
	print("x3 = " + str(x3b))
	print("Pre-set 3x1-2x2-1x3+3 as M1, 6x1-4x2+1x3+3 as M2")

