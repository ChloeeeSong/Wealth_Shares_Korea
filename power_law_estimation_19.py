import math

def open_file():
	my_file=open('korea_19.csv',"r")
	content=my_file.readlines()
	my_file.close()

	#print (content)

	data=[]
	weights=[]

	for v in content:
		my_str=v.rstrip()
		my_list=my_str.split(",")
		#print (my_list)

		data.append(float(my_list[0]))
		weights.append(float(my_list[1]))
	#print (data)
	#print (weights)

	return (data,weights)



#data=[100,90,70,66,34,21,11,9,8]
#weights=[2,4,5,8,10,12,22,26,30]

def pseudo_maximum_likelihood(data,weights):
	list_of_KS=[]
	list_of_alpha=[]
	#dic={}
	# possible candidates are from all data points except the largest one
	for i in range(20,len(data)):
		alpha = calculate_alpha(i,data,weights)
		KS = calculate_KS(alpha,i,data,weights)
		# dic={min1:(alpha1,KS1)...}
		list_of_alpha.append(alpha)
		list_of_KS.append(KS)
		#dic[data[i]] = (alpha,KS)
	data_copy=data[20:]
	return (list_of_alpha,list_of_KS,data_copy)

#x_min=data[index] is fixed
#index=8,x_min=8
#data=[100,90,70,66,34,21,11,9,8]
#alpha=N0/(N0+..+N8)log(w0/w8)+N1/(...)log(w1/w8)

def calculate_alpha(index,data,weights):

	my_sum=0
	N=sum(weights[0:index+1])
	for j in range(index+1):
		Ni=weights[j]
		wi=data[j]
		wn=data[index]
		#print (Ni/N)
		#print (wi)
		#print (wn)
		#print (math.log(wi/wn))
		my_sum+=(Ni/N)*(math.log(wi/wn))
	#print (my_sum)
	my_alpha=1/my_sum
	print (index,my_sum,my_alpha)
	return my_alpha

# alpha=2,index=3,x_min=66
#data=[100,90,70,66,34,21,11,9,8]
#weights=[2,4,5,8,10,12,22,26,30]
# [100,90,70,66]

# i=2, cdf of 70, weight_2=sum(weights[2:4]);theoretical 1-(66/70)^alpha
# i=0, cdf of 100, empirical=0, theoretical=(66/100)**alpha

def calculate_KS(alpha,index,data,weights):
	#x_min=data[index]
	max_distance=-float("inf")
	for i in range(index):
		total_weights=sum(weights[0:index+1])
		weight_i=sum(weights[i:index+1])
		s_x=weight_i/total_weights
		# ccdf of pareto with xmin and alpha
		p_x=1-(data[index]/data[i])**alpha
		distance=abs(s_x-p_x)
		if distance>max_distance:
			max_distance=distance
	return max_distance


data,weights=open_file()


alpha_list,KS_list,truncated_data= pseudo_maximum_likelihood(data,weights)
#print(alpha_list)
#print(KS_list)

minimum_distance=min(KS_list)
print (minimum_distance)

index=[]
for i in range(len(KS_list)):
	if KS_list[i]==minimum_distance:
		index.append(i)

print (index)

for i in index:
	print (truncated_data[i])
	print (alpha_list[i])








