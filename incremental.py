import matplotlib.pyplot as plt
import numpy as np

from random import randint
import pandas as pd

g1 = []
g2 = []
g3 = []
total_gener = []

def incremental_cost(demand0,change_demand):
	demand = demand0 + change_demand								#total demand needed
	const = []														#constant term after differenitation
	pterm = []														#p coeffcient after differentiation
	addlanda = 0													#term to be added to find lambda
	multiplylanda = 0												#term to be divided to find lambda

	Done = 0														#done remains at 0 until: inc cost found, generation levels found
																	#that satisfy min max requirments

	a = [ (310), (510), (78)]
	b = [ (7.25), (7.51), (7.87)]
	c = [ (0.00191), (0.00142), (0.00197)]
	pmin = [ (100), (200), (50)]
	pmax = [ (400), (600), (200)]

	for x in range (len(a)):
		const.append((b[x]))									#b term becomes differentiated constant
		pterm.append((c[x]*(2)))						#our p term is the corresponding c term divided by 2

		addlanda = addlanda + ((const[x]/pterm[x]))			#see formula
		multiplylanda = multiplylanda + (((1)/pterm[x]))
		
	landa = (demand + addlanda) / multiplylanda
	print("Incremental Cost:",landa,"$/MWh")
	print("Icremental Cost:",((landa * 100)/1000),"p/kWh")

	print("")

	power_gen = []
	total_gen = 0
	iterations = 0
	for x in range (len(a)):
		power_gen.append(((landa-const[x])/pterm[x]))		#see formula

	while(Done < len(power_gen)):									#if each gen level does not meet requirements pmin pmax stays in loop forever
		Done = 0													#initialise to 0
		for x in range (len(a)):
			if((power_gen[x]<pmin[x]) or (power_gen[x]>pmax[x])):	#requirement not met
				if(power_gen[x]<pmin[x]):							#requirment 1
					diff = pmin - power_gen[x]						#find the difference
					ranint = randint(0,len(power_gen)-1)			#choose a random generator
					power_gen[x]=power_gen[x]+diff 					#ammend incorrect gen level with the difference 
					power_gen[ranint]= power_gen[ranint] - diff     #substract difference from random generator 
					iterations = iterations + 1 
				if(power_gen[x]>pmax[x]):							#requirement 2 
					diff = power_gen[x] - pmax[x]					#difference
					ranint = randint(0,len(power_gen)-1)			#random generator chosen
					power_gen[x]=power_gen[x]-diff 					
					power_gen[ranint]= power_gen[ranint] + diff		#same steps as before	
					iterations = iterations + 1 				
			else:
				Done = Done + 1 									#if one of the generators meets the requirements, done is increased by 1
																	#until done = total number of generators (until all generators meet the requirements)
																	#loop will not	
	for x in range (len(a)):
		print("Generator",(x+1),":",power_gen[x]," MW")		
		total_gen=total_gen + power_gen[x]

	print("")	
	print("Demand Needed:",total_gen," MW")
	print("Number of Iterations:",iterations)	
	return power_gen , total_gen


case1 = incremental_cost(800,200)									#Our 5 generation cases
case2 = incremental_cost(600,200)
case3 = incremental_cost(400,200)
case4 = incremental_cost(500,200)
case5 = incremental_cost(700,200)

total_gener.append(case1[1])
total_gener.append(case2[1])
total_gener.append(case3[1])
total_gener.append(case4[1])
total_gener.append(case5[1])

for x in range(len(case1[0])):
	if(x==0):
		g1.append(case1[0][x])
		g1.append(case2[0][x])
		g1.append(case3[0][x])
		g1.append(case4[0][x])
		g1.append(case5[0][x])

	if(x==1):
		g2.append(case1[0][x])
		g2.append(case2[0][x])
		g2.append(case3[0][x])
		g2.append(case4[0][x])
		g2.append(case5[0][x])

	if(x==2):
		g3.append(case1[0][x])
		g3.append(case2[0][x])
		g3.append(case3[0][x])
		g3.append(case4[0][x])
		g3.append(case5[0][x])

N = 5
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

plt.bar(ind, np.array(g1), width=0.8, label='golds', color='red', bottom=np.array(g2)+np.array(g3))
plt.bar(ind, np.array(g2), width=0.8, label='silvers', color='blue', bottom=np.array(g3))
plt.bar(ind, np.array(g3), width=0.8, label='bronzes', color='green')

plt.ylabel('Generation MW')
plt.title('Equal Incremental Method Generator Share')
plt.xticks(ind, ('1000 MW', '800 MW', '600 MW', '700 MW', '900 MW'))
plt.yticks(np.arange(0, 1000, 100))
plt.legend((g1[0], g2[0],g3[0]), ('G1', 'G2',"G3"))

plt.show()

