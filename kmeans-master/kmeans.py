Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ###nkmeans by xinci.liu
>>> def mini_distance(dic,d1,d2):
	first_position=dic[d1]
	second_position=dic[d2]
	square_position=0
	for s in first_position:
		first=first_position[s]
		second=second_position[s]
		square_position=square_position+(first-second)**2
	distance=square_position**(1/2)
	return distance

>>> def group_first_time(diction,numbers):
	k=0
	group_cluster=[]
	D_all=[]
	for x in diction:
		D_all.append(x)
	while k<len(D_all):
		distance=100000000000000000
		i=0
		f=D_all[k]
		while i<numbers:
			d=D_all[i]
			if mini_distance(diction,d,f)<distance:
				distance=mini_distance(diction,d,f)
				group=i
			i=i+1
		a=(f,group)
		group_cluster.append(a)
		k=k+1
	return 	group_cluster

>>> def hanshu2(A,B):
    for k,v in B.items():
        A[k] = A.get(k,0)+v
    return A

>>> def new_key_list(diction,numbers,now_group):
	new_key_list=[]
	group_first=now_group
	i=0
	while i<numbers:
		initial_position={}
		num=0
		for x in group_first:
			group=x[1]
			if group==i:
				d=x[0]
				add_dic=diction[d]
				new_position=hanshu2(initial_position,add_dic)
				initial_position=new_position
				num=num+1
			else:
				initial_position=initial_position
				num=num
			for z in initial_position:
				v=initial_position[z]
				new_v=v/num
				initial_position[z]=new_v
		new_key_list.append(initial_position)
		i=i+1
	return new_key_list

>>> def distance_of_dictionary(d1,d2):
	su_m=0
	for x in d1:
		first=d1[x]
		second=d2[x]
		su_m=su_m+(first-second)**2
	distance=su_m**(1/2)
	return su_m

>>> def new_group(diction,numbers,old_group):
	group_cluster=[]
	distance=1000000000
	key_list=new_key_list(diction,numbers,old_group)
	for x in diction:
		x_position=diction[x]
		k=0
		while k<numbers:
			compare_position=key_list[k]
			if distance_of_dictionary(x_position,compare_position)<distance:
				distance=distance_of_dictionary(x_position,compare_position)
				group=k
			k=k+1
		a=(x,group)
		group_cluster.append(a)
	return 	group_cluster

>>> def stop_or_not(group,numbers):
	lis=[]
	for x in group:
		a=x[1]
		if a not in lis:
			lis.append(a)
	if len(lis)==numbers:
		return False
	else:
		return True

	
>>> def k_means(diction, numbers):
	assert numbers>1
	now_group=group_first_time(diction,numbers)
	while stop_or_not(now_group,numbers)==False:
		next_group=new_group(diction,numbers,now_group)
		return_group=now_group
		now_group=next_group
	return 	return_group

>>> diction={'d1': {'s1': 10, 's2': 1, 's3': 0}, 'd2': {'s1': 0, 's2': 0, 's3': 1},'d3':{'s1': 2, 's2': 1, 's3': 4},'d4':{'s1': 5, 's2': 4, 's3': 0},'d5':{'s1': 5, 's2': 3, 's3': 0},'d6':{'s1': 5, 's2': 3, 's3': 9},'d7':{'s1': 2, 's2': 1, 's3': 0}}
>>> k_means(diction, 4)
[('d1', 0), ('d2', 1), ('d3', 2), ('d4', 3), ('d5', 3), ('d6', 2), ('d7', 1)]
>>> k_means(diction, 1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    k_means(diction, 1)
  File "<pyshell#16>", line 2, in k_means
    assert numbers>1
AssertionError
>>> k_means(diction,3)
[('d1', 0), ('d2', 1), ('d3', 2), ('d4', 0), ('d5', 0), ('d6', 2), ('d7', 1)]
>>> 
